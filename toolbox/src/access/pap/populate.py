import json

from fastapi import UploadFile, HTTPException, File, Depends
from sqlalchemy.orm import Session
from yappl import Policy, ValidationError

from access.db import get_db
from access.db.tables import Purpose, DataObjectPurpose, DataObject
from . import router


@router.post("/upload")
async def upload_yappl_file(yappl_file: UploadFile = File(...), db: Session = Depends(get_db)):
    if yappl_file.filename.endswith('.json'):
        contents = await yappl_file.read()
        try:
            yappl_data = json.loads(contents)
            policy = Policy(yappl_data)
            policy.validate()
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON file")
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=str(e))

        for purpose in yappl_data['purposes']:
            new_purpose = Purpose(name=purpose['name'], metadata=purpose['transformations'])
            db.add(new_purpose)
            for obj in purpose['data_objects']:
                data_object = DataObject(name=obj['name'])
                db.add(data_object)
                link = DataObjectPurpose(data_object=data_object, purpose=new_purpose, active=obj['active'])
                db.add(link)
        db.commit()

        return {"detail": "Successfully populated the database with the uploaded YaPPL data."}
    else:
        raise HTTPException(status_code=400, detail="File type must be JSON.")

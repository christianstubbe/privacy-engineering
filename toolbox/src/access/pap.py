import casbin, logging
from fastapi import Request, HTTPException, APIRouter
# import utils

MODEL_PATH = "models/"
RULE_PATH = "rules/"

logger = logging.getLogger(__name__)

pap_router = APIRouter()

@pap_router.get("/policy/list")
def list_policies():
    pass

class PolicyAdministrationPoint():
    def __init__():
        pass



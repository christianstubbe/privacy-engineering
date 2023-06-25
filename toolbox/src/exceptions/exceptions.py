from fastapi import HTTPException, status


class InvalidPurposeException(HTTPException):
    def __init__(self, purpose: str):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User cannot access this data for this purpose: {purpose}",
        )

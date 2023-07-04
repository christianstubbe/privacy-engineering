import logging
from fastapi import APIRouter

logger = logging.getLogger(__name__)

pap_router = APIRouter()


class PolicyAdministrationPoint:
    def __init__(self):
        pass


pap = PolicyAdministrationPoint()


@pap_router.get("/policy/list")
def list_policies():
    pass

# TODO: list policies

# TODO: upload policies

# TODO: add a purpose

# TODO: add an exception

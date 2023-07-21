"""
This class provides an interface for Casbin to store the policy rules
"""
from casbin_sqlalchemy_adapter import Adapter
from access.db import engine

adapter = Adapter(engine)

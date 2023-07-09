import logging

import casbin
from casbin import Model
from access.adapters.alchemy import adapter
from access.models import pbac

model = Model()
model.load_model_from_text(pbac)  # This is not definitive as it could be changed 
# based on the request parameters
enforcer = casbin.Enforcer(model, adapter)
enforcer.logger.setLevel(logging.DEBUG)

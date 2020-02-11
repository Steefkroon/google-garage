# -*- coding: utf-8 -*-

from google.cloud import ndb

from shared.system.base_model.base_model import BaseModel


class Garage(BaseModel):
    """Garage is the model representation of a real world garage."""

    name = ndb.StringProperty(required=True)
    brand = ndb.StringProperty()

# -*- coding: utf-8 -*-

from shared.models.garage.garage import Garage
from shared.system import datastore
from shared.system.base_model.base_finder import BaseFinder


class GarageFinder(BaseFinder):
    """Finder class for the Garage model."""

    @classmethod
    def all_garages(cls):
        """
        Returns all garages.

        Returns:
            List(Garage]: List of query results.

        """
        with datastore.client.context():
            return Garage.query().fetch()

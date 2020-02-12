# -*- coding: utf-8 -*-

from google.cloud import ndb

from shared.system import datastore


class BaseModel(ndb.Model):
    """
    Base class for all models.

    Defines default methods that are going to be used by (almost) all models.
    """

    @property
    def key_id(self):
        """
        Shorthand method to return the integer_id of the key attribute of the object.

        Returns:
            int,None: The id of the key if the object exists in the database, else None.

        """
        if self.key:
            return self.key.integer_id()

        return None

    @classmethod
    def get(cls, key_id, parent=None):
        """
        Retrieve the entity from the database specified by key.

        Args:
            key_id (int,str): The integer id of the key.
            parent (None, ParentKey): The parent key that limits the scope of values to retrieve from.

        Returns:
            obj: An entity of the model class.

        """
        if key_id is None:
            return None
        with datastore.client.context():
            return cls.get_by_id(int(key_id), parent)

    def save(self):
        """
        Save the entity to the cloud datastore.

        Returns:
            key.Key: The key for the entity. This is always a complete key.

        """
        with datastore.client.context():
            return self.put()

    def delete(self):
        """
        Remove the entity from the datastore.

        Returns: None

        """
        with datastore.client.context():
            return self.key.delete()

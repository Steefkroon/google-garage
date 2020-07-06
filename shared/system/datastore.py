# -*- coding: utf-8 -*-

"""Module to retrieve a ndb.Client to the datastore."""

import os

import mock
from google.auth import credentials
from google.cloud import ndb


def get_client():
    """Get the client based on the environment.

    If in development environment start a client with mock credentials to access a local datastore
    If in production connect to the production datastore based on environment credentials.
    """
    # if os.environ.get('FLASK_ENV', 'production') == 'development':
    #     mock_credentials = mock.Mock(spec=credentials.Credentials)
    #     return ndb.Client(project='google-garage', credentials=mock_credentials)

    return ndb.Client()


client = get_client()

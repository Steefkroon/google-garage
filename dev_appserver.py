# -*- coding: utf-8 -*-

"""
File to run all services on one ip:port.

Also sets the database environment.
"""

# We need to import os first and then set the datastore environments, otherwise the application will crash.
import os

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

# Set development environment variables
os.environ['FLASK_ENV'] = 'development'
os.environ['DATASTORE_DATASET'] = 'google-garage'
os.environ['DATASTORE_EMULATOR_HOST'] = 'localhost:8000'
os.environ['DATASTORE_EMULATOR_HOST_PATH'] = 'localhost:8000/datastore'
os.environ['DATASTORE_HOST'] = 'http://localhost:8000'
os.environ['DATASTORE_PROJECT_ID'] = 'google-garage'

# Import all services.
from app.main import app

HOSTNAME = 'localhost'
PORT = 8080

application = DispatcherMiddleware(
    app, {
    },
)

if __name__ == '__main__':
    run_simple(
        hostname=HOSTNAME,
        port=PORT,
        application=application,
        use_reloader=True,
        use_debugger=True,
        use_evalex=True,
    )

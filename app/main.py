# -*- coding: utf-8 -*-

from flask import Flask, render_template

from app.handlers import garages

app = Flask(__name__)
app.register_blueprint(garages.bp)


@app.route('/')
def index():
    """
    Render the default index.html after which Vue runs the rest of the frontend application.

    Returns: Template

    """
    return render_template('index.html')

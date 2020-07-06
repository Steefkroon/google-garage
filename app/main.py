# -*- coding: utf-8 -*-

from flask import Flask, render_template
from werkzeug.routing import BaseConverter

from app.handlers import garages
from shared.system.handlers.lazyview import LazyView

class StringWithoutDotConverter(BaseConverter):
    regex = "[^./]+"

app = Flask(__name__)
app.url_map.strict_slashes = False
app.url_map.converters['nodot'] = StringWithoutDotConverter
# app.register_blueprint(garages.bp)


def url(url_rules, import_name, method_name, **options):
    view = LazyView(import_name, method_name)
    for url_rule in url_rules:
        app.add_url_rule(url_rule, view_func=view,  **options)


url(['/garage-list/'], 'app.handlers.garages.GarageView', 'list')
url(['/garage-list/delete/<path:rest>'], 'app.handlers.garages.GarageView', 'andere_list')


@app.route('/')
def index():
    """
    Render the default index.html after which Vue runs the rest of the frontend application.

    Returns: Template

    """
    return render_template('index.html')

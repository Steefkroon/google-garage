# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, make_response, redirect
from flask.views import View

from shared.models.garage.garage_finder import GarageFinder

bp = Blueprint(name='garages', import_name=__name__, url_prefix='/garages')


class GarageView:

    def __init__(self):
        self.response = make_response()
        print(request.args)

    def run_before(self, *args, **kwargs):
        return None

    def list(self, name='deleted'):
        self.response.headers['Content-Type'] = 'application/json; charset="utf-8"'
        self.response.data = 'Hallo'
        return self.response


    def andere_list(self):
        return jsonify(
            'andere list'
        )

# @bp.route('/', methods=['GET'])
# def list_garages():
#     """
#     Returns a list of garages in JSON format.
#
#     Returns: JSON
#     """
#     return jsonify(
#         [{
#             'id': garage.key_id,
#             'name': garage.name,
#             'brand': garage.brand,
#         } for garage in GarageFinder.all_garages()
#         ],
#     )

# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify

from shared.models.garage.garage_finder import GarageFinder

bp = Blueprint(name='garages', import_name=__name__, url_prefix='/garages')


@bp.route('/', methods=['GET'])
def list_garages():
    """
    Returns a list of garages in JSON format.

    Returns: JSON
    """
    return jsonify(
        [{
            'id': garage.key_id,
            'name': garage.name,
            'brand': garage.brand,
        } for garage in GarageFinder.all_garages()
        ],
    )

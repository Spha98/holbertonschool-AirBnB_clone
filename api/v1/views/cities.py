#!/usr/bin/env python3
"""HolbertonBnB City view."""
from api.v1.views import app_views
from flask import abort, jsonify, request
from flasgger import swag_from
from models import storage
from models.city import City


@app_views.route("/states/<state_id>/cities", methods=["GET", "POST"])
@swag_from("../apidocs/cities/get_cities.yml", methods=["GET"])
@swag_from("../apidocs/cities/post.yml", methods=["POST"])
def cities_by_state(state_id):
    """Defines GET and POST methods for cities on the states route.
    GET - Retrieve a list of City objects related to a given State.
    POST - Creates a City.
    """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)

    # GET method
    if request.method == "GET":
        return jsonify([city.to_dict() for city in state.cities])

    # POST method
    data = request.get_json(silent=True)
    if data is None:
        return "Not a JSON", 400
    if data.get("name") is None:
        return "Missing name", 400
    data["state_id"] = state_id
    city = City(**data)
    city.save()
    return jsonify(city.to_dict()), 201

#!/usr/bin/env python3
"""HolbertonBnB State view."""
from api.v1.views import app_views
from flask import abort, jsonify, request
from flasgger import swag_from
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET", "POST"])
@swag_from("../apidocs/states/get_states.yml", methods=["GET"])
@swag_from("../apidocs/states/post.yml", methods=["POST"])
def states():
    """Defines GET and POST methods for the states route.
    GET - Retrives a list of all State objects.
    POST - Creates a State.
    """
    # GET method
    if request.method == "GET":
        return jsonify([s.to_dict() for s in storage.all("State").values()])

    # POST method
    data = request.get_json(silent=True)
    if data is None:
        return "Not a JSON", 400
    if data.get("name") is None:
        return "Missing name", 400
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["GET", "DELETE", "PUT"])
@swag_from("../apidocs/states/get_state_id.yml", methods=["GET"])
@swag_from("../apidocs/states/delete.yml", methods=["DELETE"])
@swag_from("../apidocs/states/put.yml", methods=["PUT"])
def state_id(state_id):
    """Defines GET, DELETE and PUT methods for a specific ID on states.

#!/usr/bin/env python3
"""HolbertonBnB User view."""
from api.v1.views import app_views
from flask import abort, jsonify, request
from flasgger import swag_from
from models import storage
from models.user import User


@app_views.route("/users", methods=["GET", "POST"])
@swag_from("../apidocs/users/get_users.yml", methods=["GET"])
@swag_from("../apidocs/users/post.yml", methods=["POST"])
def users():
    """Defines GET and POST methods for the /users route.
    GET - Retrievs a list of all User objects.
    POST - Creates a User.
    """
    # GET method
    if request.method == "GET":
        return jsonify([u.to_dict() for u in storage.all("User").values()])

    # POST method
    data = request.get_json(silent=True)
    if data is None:
        return "Not a JSON", 400
    if data.get("email") is None:
        return "Missing email", 400
    if data.get("password") is None:
        return "Missing password", 400
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

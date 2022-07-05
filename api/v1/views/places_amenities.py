#!/usr/bin/env python3
"""Defines the view for places amenities Api calls"""
import os
from flask import abort, jsonify, request
from flasgger import swag_from
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route("/places/<place_id>/amenities", methods=["GET"])
@swag_from("../apidocs/places_amenities/get.yml")
def show_place_amenities(place_id):
    """Defines the GET method for getting a list of amenities
    from a place on id
    GET - Retrives amenities from a place based on id
    """
    place = storage.get("Place", place_id)

    if place is None:
        abort(404)
    return jsonify([a.to_dict() for a in place.amenities])


@app_views.route(
    "/places/<place_id>/amenities/<amenity_id>",
    methods=["POST", "DELETE"]
)
@swag_from("../apidocs/places_amenities/post.yml", methods=["POST"])
@swag_from("../apidocs/places_amenities/delete.yml", methods=["DELETE"])
def manage_place_amenities(place_id, amenity_id):
    """Defines the POST and DELETE methods for a Amenity object
    for a Place object
    DELETE - remote an Amenity object from a place based on id
    POST - Addes an Amenity object from a place based on id
    """
    place = storage.get("Place", place_id)
    amenity = storage.get("Amenity", amenity_id)
    exists = False
    if place is None or amenity is None:
        abort(404)

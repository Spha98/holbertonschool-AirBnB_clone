#!/usr/bin/env python3
"""Defines a status route for the HolbertonBnB API."""
from flask import jsonify
from flasgger import swag_from
from models import storage
from api.v1.views import app_views


@app_views.route("/status")
@swag_from("../apidocs/status/status.yml")
def status():
    """Returns the server status.
    Returns:
        JSON object with the current server status.
    """
    return jsonify({"status": "OK"})

#!/usr/bin/env python3
"""HolbertonBnB main Flask application.

The application listens on host IP 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
"""
import uuid
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session after each request."""
    storage.close()




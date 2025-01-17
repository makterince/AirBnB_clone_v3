#!/usr/bin/python3
""" registers blueprints"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_appcontext(exception):
    """calls for storage"""


    storage.close()

@app.errorhandler(404)
def not_found(e):
    """ configures error 404 replies """


    return jsonify({"error": "Not found"}), e.code

if __name__ == "__main__":

    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)

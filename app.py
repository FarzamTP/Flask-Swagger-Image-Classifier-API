#! /usr/bin/python3

from flask import Flask, make_response, jsonify
from settings import *
from routes import request_api
from flask_swagger_ui import get_swaggerui_blueprint


APP = Flask(__name__)

@APP.errorhandler(400)
def handle_error_400(error):
    return make_response(jsonify({'error': 'Misunderstood'}), 400)

@APP.errorhandler(401)
def handle_error_401(error):
    return make_response(jsonify({'error': 'Unauthorized'}), 401)

@APP.errorhandler(404)
def handle_error_404(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@APP.errorhandler(500)
def handle_error_500(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

### swagger specific ###
SWAGGER_URL = '/ui'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

APP.register_blueprint(request_api.get_blueprint())

if __name__ == "__main__":
    APP.run(host=HOST, port=PORT)


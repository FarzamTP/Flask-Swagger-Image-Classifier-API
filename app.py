#! /usr/bin/python3

from flask import Flask, make_response, jsonify
from settings import *


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

if __name__ == "__main__":
    APP.run(host=HOST, port=PORT)


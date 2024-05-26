#!/usr/bin/python3
"""web api"""

from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

app.register_blueprint(app_views)


if __name__ == '__main__':
    app_ho = getenv('HBNB_API_HOST', '0.0.0.0')
    app_po = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=app_ho, port=app_po, threaded=True)
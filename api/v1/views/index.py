#!/usr/bin/python3
"""app_view app"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status_api():
    """
    returns a JSON: "status": "OK"
    """
    res = {'status': "OK"}
    return jsonify(res)
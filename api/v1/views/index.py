#!/usr/bin/python3
'''
    flask with general routes
    routes:
        /status:    display "status":"OK"
        /stats:     dispaly total for all classes
'''
from  . import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'])
def api_status():
    return jsonify({"status": "OK"})
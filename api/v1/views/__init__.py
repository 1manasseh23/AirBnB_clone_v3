from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


"""import storage engine and classes"""
from models import storage

"""import flask views"""
from api.v1.views.index import *


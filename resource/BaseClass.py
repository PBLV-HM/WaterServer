from flask.views import MethodView
from flask_restful import Resource
from sqlalchemy import create_engine
from sqlalch import Base
from sqlalchemy.orm import sessionmaker
from sqlalch import User as users

class WaterBase(MethodView):
    mysqlconnection = None

import datetime
from flask import g
from sqlalchemy.sql import select

from flaskBase import auth, db
from resource.data import get_data_from_sql
from sqlalch import Groups as groups, Data
from BaseClass import WaterBase
from flask import request
import json
from flask_restful import reqparse, marshal, fields, marshal_with, abort

char_data_fields = {
    'label': fields.String,
    'value': fields.Float,
}

coord_data_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'latitude': fields.Float,
    'longitude': fields.Float,
}

device_data_fields = {
    'degree': fields.List(fields.Nested(char_data_fields)),
    'dist': fields.List(fields.Nested(char_data_fields)),
    'wet': fields.List(fields.Nested(char_data_fields)),
    'coords': fields.List(fields.Nested(coord_data_fields))
}

class DeviceData(WaterBase):
    decorators = [auth.login_required]

    def get(self, id, interval):
        sql = Data.sql_data_query_device(interval, g.user.id, id)
        data = get_data_from_sql(sql)
        return marshal(data, device_data_fields)
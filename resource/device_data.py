import datetime
from flask import g
from sqlalchemy.sql import select

from flaskBase import auth, db
from sqlalch import Groups as groups, Data
from BaseClass import WaterBase
from flask import request
import json
from flask_restful import reqparse, marshal, fields, marshal_with, abort

char_data_fields = {
    'label': fields.String,
    'value': fields.Float,
}

device_data_fields = {
    'degree': fields.List(fields.Nested(char_data_fields)),
    'dist': fields.List(fields.Nested(char_data_fields)),
    'wet': fields.List(fields.Nested(char_data_fields)),
}

class DeviceData(WaterBase):
    decorators = [auth.login_required]

    def get(self, id, interval):
        sql = Data.sql_data_query(interval, g.user.id)

        result = db.engine.execute(sql)

        deg_data = [];
        wet_data = [];
        dist_data = [];
        for row in result:
            deg_data.append({"label": row.time_interval, "value": row.degree})
            wet_data.append({"label": row.time_interval, "value": row.wet})
            dist_data.append({"label": row.time_interval, "value": row.dist})

        data = {'degree': deg_data, 'dist': dist_data, 'wet': wet_data}
        return marshal(data, device_data_fields)
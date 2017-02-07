import datetime
from flask import g
from sqlalchemy.sql import select

from flaskBase import auth, db
from sqlalch import Groups as groups, Data
from BaseClass import WaterBase
from flask import request
import json
from flask_restful import reqparse, marshal, fields, marshal_with, abort

device_data_fields = {
    'time_interval': fields.String,
    'degree': fields.Float,
    'dist': fields.Float,
    'wet': fields.Float
}

class DeviceData(WaterBase):
    decorators = [auth.login_required]

    def get(self, id, time_from):
        tfrom = datetime.datetime.fromtimestamp(int(time_from))
        sql = Data.sql_data_query(5, g.user.id)

        result = db.engine.execute(sql)

        return [marshal(data, device_data_fields) for data in result]
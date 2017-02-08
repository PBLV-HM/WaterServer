from flask import g
from sqlalchemy.sql import select

from flaskBase import auth, db
from resource.data import Data, get_data_from_sql
from resource.device_data import device_data_fields
from sqlalch import Groups as groups
from BaseClass import WaterBase
from flask import request
import json
from flask_restful import reqparse, marshal, fields, marshal_with, abort

class GroupData(WaterBase):
    decorators = [auth.login_required]

    def get(self, id, interval):
        sql = Data.sql_data_query_device(interval, g.user.id, id)
        data = get_data_from_sql(sql)
        return marshal(data, device_data_fields)
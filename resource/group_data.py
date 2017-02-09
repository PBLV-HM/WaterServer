from datetime import datetime

from dateutil import parser
from flask import g
from sqlalchemy.sql import select

from flaskBase import auth, db
from resource.data import get_data_from_sql
from resource.device_data import device_data_fields
from sqlalch import Groups as groups, Data
from BaseClass import WaterBase
from flask import request
import json
from flask_restful import reqparse, marshal, fields, marshal_with, abort

class GroupData(WaterBase):
    decorators = [auth.login_required]

    def get(self, id, interval):
        sql = Data.sql_data_query_group(interval, g.user.id, id)
        data = get_data_from_sql(sql)

        last_time = data['degree'][0]['label']
        parse_time = datetime.strptime(last_time, '%d.%m.%y %H:%M')

        sql = Data.sql_coord_query_group(g.user.id, id, str(parse_time))
        coords = db.engine.execute(sql)

        data['coords'] = []
        i = 0

        for c in coords:
            items = dict(c.items())
            items['id'] = i
            i += 1
            data['coords'].append(items)

        return marshal(data, device_data_fields)
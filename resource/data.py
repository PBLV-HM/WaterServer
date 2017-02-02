from BaseClass import WaterBase
from flask import request
import sqlalch
import dateutil.parser


class Data(WaterBase):

    def post(self):
        a = request.get_json()

        session = self.getsession

        data2 = sqlalch.Data()

        data2.lat = a['lat']
        data2.lon = a['lon']
        data2.devID = a['id']
        data2.timestamp = dateutil.parser.parse(a['timestamp'])
        data2.degree = a['deg']
        session.add(data2)
        session.commit()

        print a
        return("200 OK")
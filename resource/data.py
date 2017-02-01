from BaseClass import WaterBase
from flask import request
from sqlalch import Data
from datetime import datetime
import dateutil.parser
from sqlalch import Base
from sqlalchemy.orm import sessionmaker

class Data(WaterBase):

    def post(self):
        a = request.get_json()

        session = self.getsession

        data2 = Data()

        data2.lat = a['lat']
        data2.lon = a['lon']
        data2.devID = a['id']
        data2.timestamp = a['timestamp']
        data2.degree = a['deg']
        session.add(data2)
        session.commit()

        print a
        return("200 OK")
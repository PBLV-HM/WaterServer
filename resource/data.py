from datetime import datetime

from flask_restful import reqparse, marshal, fields, marshal_with
from BaseClass import WaterBase
from flaskBase import request, db
from sqlalch import Device as devices
import sqlalch
import dateutil.parser

data_fields = {
    'devId': fields.Integer,
    'lat': fields.Float,
    'lon': fields.Float,
    'degree': fields.Float,
    'distance': fields.Float,
    'airpressure': fields.Integer,
    'wet': fields.Integer,
}

def get_data_from_sql(sql):
    result = db.engine.execute(sql)

    deg_data = [];
    wet_data = [];
    dist_data = [];

    for row in result:
        time = datetime.fromtimestamp(row.time_interval).strftime('%d.%m.%y %H:%M')
        dist = row.normPeg - row.dist
        deg_data.append({"label": time, "value": round(row.degree, 1)})
        wet_data.append({"label": time, "value": round(row.wet, 1)})
        dist_data.append({"label": time, "value": round(dist, 1)})

    return {'degree': deg_data[::-1], 'dist': dist_data[::-1], 'wet': wet_data[::-1]}

class Data(WaterBase):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('lat', type=float, location='json')
        self.reqparse.add_argument('lon', type=float, location='json')
        self.reqparse.add_argument('degree', type=float, location='json', required=True)
        self.reqparse.add_argument('distance', type=float, location='json', required=True)
        self.reqparse.add_argument('wet', type=int, location='json', required=True)

    def get(self, id):
        all_data = db.session.query(sqlalch.Data).filter(sqlalch.Data.devID == id).all()
        return [marshal(data, data_fields) for data in all_data]

    @marshal_with(data_fields)
    def post(self, id):
        args = self.reqparse.parse_args()

        if args['distance'] > 400:
            return "Distance to high", 400

        dev = db.session.query(devices).filter(devices.id == id).first()
        if dev is None:
            return "Device not found", 404

        data = sqlalch.Data(devID = id,
                            lat = args['lat'],
                            lon = args['lon'],
                            degree = args['degree'],
                            distance = args['distance'],
                            wet = args['wet'])

        db.session.add(data)
        db.session.commit()

        return data, 201






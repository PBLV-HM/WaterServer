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


class Data(WaterBase):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('lat', type=float, location='json', required=True)
        self.reqparse.add_argument('lon', type=float, location='json', required=True)
        self.reqparse.add_argument('degree', type=float, location='json', required=True)
        self.reqparse.add_argument('distance', type=float, location='json', required=True)
        self.reqparse.add_argument('wet', type=int, location='json', required=True)

    def get(self, id):
        all_data = db.session.query(sqlalch.Data).filter(sqlalch.Data.devID == id).all()
        return [marshal(data, data_fields) for data in all_data]

    @marshal_with(data_fields)
    def post(self, id):
        args = self.reqparse.parse_args()

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






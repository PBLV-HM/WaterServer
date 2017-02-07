from flask import g
from flask_restful import reqparse, marshal, fields, marshal_with, abort
from flaskBase import auth, db
from sqlalch import Device as devices
from resource.BaseClass import WaterBase
from resource.device import device_fields


class DeviceList(WaterBase):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json', required=True)
        self.reqparse.add_argument('name', type=str, location='json', required=True)
        self.reqparse.add_argument('active', type=bool, location='json', required=True)

    def get(self):
        userid = g.user.id
        alldata = db.session.query(devices).filter(devices.userId == userid)

        return [marshal(data, device_fields) for data in alldata]


    @marshal_with(device_fields)
    def post(self):
        args = self.reqparse.parse_args()
        device = devices(id = args['id'],
                         name = args['name'],
                         active = args['active'],
                         userId = g.user.id)

        db.session.add(device)
        db.session.commit()

        return device, 201
from flask import g
from flask_restful import reqparse, marshal, fields, marshal_with, abort

from flaskBase import auth, db
from sqlalch import Device as devices
from BaseClass import WaterBase
from flask import request

device_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'userId': fields.Integer,
    'active': fields.Boolean
}


class Device(WaterBase):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json', required=True)
        self.reqparse.add_argument('active', type=bool, location='json', required=True)

    def get(self, id):
        userid = g.user.id
        alldata = db.session.query(devices).filter(devices.userId == userid).filter(devices.id == id).one()

        return alldata

    def put(self, id):
        args = self.reqparse.parse_args()
        userid = g.user.id
        device = db.session.query(devices)\
            .filter(devices.userId == userid)\
            .filter(devices.id == id)

        if device:
            device.update({"name": args['name'],"active": args['active']});
            db.session.commit()
            return {}, 201
        else:
            return {}, 404

    def delete(self, id):
        userid = g.user.id
        device = db.session.query(devices)\
            .filter(devices.userId == userid)\
            .filter(devices.id == id).first()
        if not device:
            abort(404)
        db.session.delete(device)
        db.session.commit()
        return {}, 204
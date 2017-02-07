from flask import g
from sqlalchemy.sql import select

from flaskBase import auth, db
from sqlalch import Groups as groups, GroupEntry
from BaseClass import WaterBase
from flask import request
import json
from flask_restful import reqparse, marshal, fields, marshal_with, abort

class DeviceJoin(WaterBase):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('normPeg', type=float, location='json', required=True)
        self.reqparse.add_argument('grpId', type=int, location='json', required=True)

    def post(self, id):
        args = self.reqparse.parse_args()
        new_group = GroupEntry(devID = id,
                            grpID = args["grpId"],
                            normPeg = args["normPeg"],
                            userId = g.user.id)

        db.session.add(new_group)
        db.session.commit()

        return {}, 201

    def delete(self, id):
        new_group = GroupEntry(grpId = 0,
                                devId = id,
                                userId = g.user.id)

        db.session.add(new_group)
        db.session.commit()
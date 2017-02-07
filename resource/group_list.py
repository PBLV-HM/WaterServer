from flask import g
from sqlalchemy.sql import select

from flaskBase import auth, db
from resource.group import group_fields
from sqlalch import Groups as groups
from BaseClass import WaterBase
from flask import request
import json
from flask_restful import reqparse, marshal, fields, marshal_with, abort

class GroupList(WaterBase):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json', required=True)
        self.reqparse.add_argument('state', type=bool, location='json', required=True)

    def get(self):
        all_groups = db.session.query(groups).filter(groups.userId == g.user.id).all()
        return [marshal(task, group_fields) for task in all_groups]

    @marshal_with(group_fields)
    def post(self):
        args = self.reqparse.parse_args()
        device = groups(name = args['name'],
                        state = args['state'],
                        userId = g.user.id)

        db.session.add(device)
        db.session.commit()

        return device, 201
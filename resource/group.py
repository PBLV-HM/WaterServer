from flask import g
from sqlalchemy.sql import select

from flaskBase import auth, db
from sqlalch import Groups as groups
from BaseClass import WaterBase
from flask import request
import json
from flask_restful import reqparse, marshal, fields, marshal_with, abort

group_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'state': fields.Boolean
}

class Group(WaterBase):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json', required=True)
        self.reqparse.add_argument('state', type=bool, location='json', required=True)

    def put(self, id):
        args = self.reqparse.parse_args()
        userid = g.user.id
        group = db.session.query(groups)\
            .filter(groups.userId == userid)\
            .filter(groups.id == id)

        if group:
            group.update({"name": args['name'],"state": args['state']});
            db.session.commit()
            return {}, 201
        else:
            return {}, 404

    def delete(self, id):
        userid = g.user.id
        group = db.session.query(groups)\
            .filter(groups.userId == userid)\
            .filter(groups.id == id).first()

        if not group:
            abort(404)

        db.session.delete(group)
        db.session.commit()
        return {}, 204
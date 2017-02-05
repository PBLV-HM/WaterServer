from flask_restful import reqparse, marshal, fields
from BaseClass import WaterBase
from flaskBase import db
from sqlalch import User as users
import json
from flask import request

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'lastname': fields.String,
    'firstname': fields.String
}

class User(WaterBase):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('firstname', type=str, location='json')
        self.reqparse.add_argument('lastname', type=str, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        self.reqparse.add_argument('username', type=str, location='json')

    def post(self):
        args = self.reqparse.parse_args()

        userdata = users(firstname = args['firstname'],
                         lastname = args['lastname'],
                         username = args['username'])
        userdata.hash_password(args['password']);

        db.session.add(userdata)
        db.session.commit()

        return marshal(userdata, user_fields), 201

    def get(self):
        userid = request.args.get('user')
        if userid:
            user = db.session.query(users).filter(users.id == userid).one()
            return marshal(user, user_fields)
        else:
            all_user = db.session.query(users).all()
            return [marshal(task, user_fields) for task in all_user]

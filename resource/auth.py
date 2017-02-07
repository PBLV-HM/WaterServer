from flask import g, jsonify
from flask_restful import marshal

from BaseClass import WaterBase
from flaskBase import auth
from resource.user import user_fields
from sqlalch import User


class Auth(WaterBase):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        return jsonify({'token': token.decode('ascii'), 'user': marshal(g.user, user_fields)})

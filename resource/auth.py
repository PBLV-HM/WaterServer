from flask import g, jsonify
from BaseClass import WaterBase
from flaskBase import auth
from sqlalch import User


class Auth(WaterBase):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        return jsonify({'token': token.decode('ascii')})

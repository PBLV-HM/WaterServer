from flask_httpauth import HTTPBasicAuth
from BaseClass import WaterBase as base
from sqlalch import User as users

from server import auth

@auth.verify_password
def verify_password(username, password):
    session = base.getsession
    data = session.query(users).get(username)
    userdata = data.__dict__
    if userdata:
        return userdata['password']
    return None


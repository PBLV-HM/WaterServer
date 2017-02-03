from BaseClass import WaterBase
from sqlalch import User as users
import json
from flask import request

class User(WaterBase):

    def post(self):
        a = request.get_json()
        session = self.getsession
        userdata = users()

        userdata.firstname = a['firstname']
        userdata.lastname = a['lastname']
        userdata.password_hash = a['password']
        userdata.username = a['username']
        session.add(userdata)
        session.commit()

        return "200 OK"

    def get(self):
        username = request.args.get('user')
        session = self.getsession

        data = session.query(users).filter(users.username == username).one()
        b = data.__dict__
        del b['_sa_instance_state']
        return json.dumps(b)
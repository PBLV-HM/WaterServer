from BaseClass import WaterBase
from sqlalch import User as users
import json

class User(WaterBase):

    def post(self):
        a = request.get_json()
        session = self.getsession
        userdata = users()

        userdata.firstname = a['firstname']
        userdata.lastname = a['lastname']
        userdata.password = a['password']
        userdata.username = a['username']
        session.add(userdata)
        session.commit()

        return "200 OK"

    def get(self):
        username = request.args.get('user')
        session = self.getsession

        data = session.query(users).get(username)
        b = data.__dict__
        del b['_sa_instance_state']
        return json.dumps(b)
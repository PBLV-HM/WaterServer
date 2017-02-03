from BaseClass import WaterBase

from sqlalch import User as users
import json
from flask import request


class Info(WaterBase):
    def get(self):
        return "This API has the following Endpoints: \n" \
               "setGroup<DeviceID/GroupName>" \
               "sets a device as member of the specified group \n" \
               "getGroup/<DeviceID>" \
               "see which group the device has been member of" \
               "groupInfo<GroupName, Timestamp>" \
               "gets all datasets for the specified group from timestamp up to the days specified. \n" \
               "if no day is specified: days = 4" \
               ""

    def post(self):
        a = request.get_json()

        session = self.getsession
        data = session.query(users).filter(users.username == username).one()
        b = data.__dict__
        del b['_sa_instance_state']

        if a['password'] == b['password_hash']:
            return json.dumps(b)
        else:
            return unauthenticated

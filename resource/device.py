from sqlalchemy.sql import select
from sqlalch import Device as devices
from BaseClass import WaterBase
from flask import request
import json

class Device(WaterBase):
    def post(self):
        a = request.get_json()
        session = self.getsession
        dev = devices()

        dev.id = a['id']
        dev.name = a['name']
        dev.userId = a['userId']
        dev.active = bool(a['active'])
        session.add(dev)
        session.commit()

    def get(self):
        username = request.args.get('user')
        session = self.getsession


        data = session.query(devices).filter(devices.name == username)
        userDevices = []
        for i in data:
            temp = i.__dict__
            del temp['_sa_instance_state']
            userDevices.append(temp)

        b = {"devices": userDevices}
        return json.dumps(b)

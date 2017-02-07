from flask import g
from flask.ext.restful import marshal

from flaskBase import auth, db
from sqlalch import Device as devices
from resource.BaseClass import WaterBase
from resource.device import device_fields


class DeviceList(WaterBase):
    decorators = [auth.login_required]

    def get(self):
        userid = g.user.id
        alldata = db.session.query(devices).filter(devices.userId == userid)

        return [marshal(data, device_fields) for data in alldata]
from sqlalchemy.sql import select
from sqlalch import Groups as groups
from BaseClass import WaterBase
from flask import request
import json

class Group(WaterBase):
    def post(self):
        session = self.getsession
        a = request.get_json()

        grp = groups()
        grp.grpName=a['grpname']
        grp.grpState = bool(a['state'])
        grp.user = a['user']

        session.add(grp)
        session.commit
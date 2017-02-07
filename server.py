from flaskBase import g, api, app, auth
from resource.auth import Auth as RAuth
from resource.device_join import DeviceJoin
from resource.device_list import DeviceList
from resource.group_list import GroupList
from resource.data import Data
from resource.device import Device
from resource.group import Group
from resource.user import User as Userquery
from sqlalch import User

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

api.add_resource(Userquery, '/user')
api.add_resource(Device, '/device/<int:id>')
api.add_resource(DeviceList, '/device')
api.add_resource(DeviceJoin, '/device/join/<int:id>')
api.add_resource(RAuth, '/auth')
api.add_resource(Data, '/data/<int:id>')
api.add_resource(GroupList, '/group')
api.add_resource(Group, '/group/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, port=63837, host='0.0.0.0')

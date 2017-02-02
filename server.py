from flask_restful import abort

from flaskBase import g, api, app, auth

from resource.auth import Auth as RAuth
from resource.info import Info
from resource.data import Data
#from resource.user import User
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


api.add_resource(Info, '/info')
api.add_resource(Data, '/data')
api.add_resource(RAuth, '/auth')
#api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
import flask_restful as restful
from resource.info import Info
from resource.data import Data
from resource.user import User
from server import auth


from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(Info, '/info')
api.add_resource(Data, '/data')
api.add_resource(User, '/user')


if __name__ == '__main__':
    app.run(debug=True)

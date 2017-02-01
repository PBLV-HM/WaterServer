from flask import Flask
import flask_restful as restful
from resource.info import Info
from resource.data import Data

import sqlalchemy

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(Info, '/info')
api.add_resource(Data, '/data')







if __name__ == '__main__':
    app.run(debug=True)

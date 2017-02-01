from flask import Flask
import datetime
from flask import request
from flask import json
import flask_restful as restful
from resource.info import Info

import sqlalchemy

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(Info, '/info')






if __name__ == '__main__':
    app.run(debug=True)

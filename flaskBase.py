from flask import Flask, abort, request, jsonify, g, url_for
from flask import logging
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
import flask_restful as restful

app = Flask(__name__)
CORS(app)
logging.getLogger('flask_cors').level = logging.DEBUG


# initialization
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@127.0.0.1/hmpblv'
app.config['SQLALCHEMY_ECHO'] = True
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = restful.Api(app)

# extensions
db = SQLAlchemy(app)
auth = HTTPBasicAuth()
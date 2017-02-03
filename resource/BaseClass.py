from flask.views import MethodView
from flask_restful import Resource
from sqlalchemy import create_engine
from sqlalch import Base
from sqlalchemy.orm import sessionmaker
from sqlalch import User as users

class WaterBase(MethodView):
    mysqlconnection = None
    mysqlsession = None

    def __init__(self):
        global mysqlconnection
        global mysqlsession
        mysqlconnection = None
        mysqlsession = None

    @property
    def mysqlconn(self):
        global mysqlconnection
        global mysqlsession
        if mysqlconnection:
            return mysqlconnection
        else:
            mysqlconnection = create_engine('mysql://hmpblv:ahs7ThasaiMioj@localhost/hmpblv')
            Base.metadata.bind = mysqlconnection
            return mysqlconnection


    @property
    def getsession(self):
        global mysqlconnection
        global mysqlsession

        if mysqlsession:
            return mysqlsession
        else:
            session = sessionmaker()
            session.configure(bind=self.mysqlconn)
            mysqlsession = session()
            return mysqlsession

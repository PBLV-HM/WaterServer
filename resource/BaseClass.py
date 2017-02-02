from flask.views import MethodView
from flask_restful import Resource
from sqlalchemy import create_engine
from sqlalch import Base
from sqlalchemy.orm import sessionmaker
from sqlalch import User as users

class WaterBase(MethodView):
    mysqlconnection = None
    mysqlsession = None

    @property
    def mysqlconn(self):
        if self.mysqlconnection:
            return self.mysqlconnection
        else:
            self.mysqlconnection = create_engine('mysql://root@localhost/hmpblv')
            Base.metadata.bind = self.mysqlconnection
            return self.mysqlconnection


    @property
    def getsession(self):
        if self.mysqlsession:
            return self.mysqlsession
        else:
            session = sessionmaker()
            session.configure(bind=self.mysqlconn)
            self.mysqlsession = session()
            return self.mysqlsession
from flask.views import MethodView
from sqlalchemy import create_engine, engine
from sqlalch import Base
from sqlalch import Base, Data
from sqlalchemy.orm import sessionmaker


class WaterBase(MethodView):
    mysqlconnection = None;
    mysqlsession = None;

    @property
    def mysqlconn(self):
        if self.mysqlconnection:
            return self.mysqlconnection
        else:
            self.mysqlconnection = create_engine('mysql://hmpblv:ahs7ThasaiMioj@localhost/hmpblv')
            Base.metadata.bind = self.mysqlconnection
            return self.mysqlconnection


    @property
    def getsession(self):
        if self.mysqlsession:
            return self.mysqlsession
        else:
            session = sessionmaker(bind=self.mysqlconnection)
            self.mysqlsession = session()
            return self.mysqlsession
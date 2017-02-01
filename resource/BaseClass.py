from flask.views import MethodView

from sqlalchemy import create_engine, engine
class WaterBase(MethodView):

    mysqlconnection = None;

    @property
    def mysqlconn(self):
        if self.mysqlconnection:
            return self.mysqlconnection
        else:
            mysqlconnection = create_engine('mysql://hmpblv:ahs7ThasaiMioj@localhost/hmpblv')
            return mysqlconnection



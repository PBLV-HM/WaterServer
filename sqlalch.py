from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, PrimaryKeyConstraint, Float, Boolean

Base = declarative_base()
class Device(Base):
    __tablename__ = 'Device'
    id = Column(String(32), primary_key=True, nullable=False)
    name = Column(String(50))
    userId = Column('userId', Integer, ForeignKey("User.id"))

    def __repr__(self):
        return "<id(id='%s', name='%s')>" % (self.id, self.name)


class GroupEntry(Base):
    __tablename__ = 'GroupEntry'
    grpID = Column('grpID', Integer, ForeignKey("Group.grpID"), nullable=False)
    devID = Column('devID', String(32), ForeignKey("Device.id"), nullable=False, primary_key=True)
    timestamp = Column('timestamp', DateTime, nullable=False, primary_key=True)
    normPeg = Column('normPeg', Float)
    PrimaryKeyConstraint('devID', 'timestamp')
    def __repr__(self):
        return "<GroupEntrie(grpID='%s', timestamp='%s', devID='%s')>" % (
                                self.grpID, self.timestamp, self.devID)

class Group(Base):
    __tablename__ = 'Group'
    grpName = Column('grpName', String(32), nullable=False)
    grpID = Column('grpID', Integer, primary_key=True, nullable=False, autoincrement=True)
    grpState = Column ('grpState', Boolean, nullable=False)

    def __repr__(self):
        return "<Group(grpID='%s', grpName='%s', devID='%s', grpState='%s')>" % (
                                self.grpID, self.grpName, self.grpState)

class Data(Base):
    __tablename__ = 'Data'
    devID = Column('devID', String(32), nullable=False, primary_key=True)
    timestamp = Column('timestamp', DateTime, nullable=False, primary_key=True)
    PrimaryKeyConstraint('devID', 'timestamp')
    lon = Column('lon', Float)
    lat = Column('lat', Float)
    degree = Column('degree', Integer)
    distance = Column('deg', Float)
    airpressure = Column('airpressure', Integer)
    wet = Column('wet', Integer)

class User(Base):
    __tablename__ = 'User'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(32), index = True, nullable=False)
    password = Column('password', String(72), nullable=False)
    token = Column('token', String(32))
    firstname = Column('firstname', String(32))
    lastname = Column('lastname', String(32))

    def __repr__(self):
        #return "<User(username='%s', password='%s', token='%s', firstname='%s', lastname='%s')>" % (
        #                        self.username, self.password, self.token, self.firstname, self.lastname)
        return {"id": self.id, "username":self.username, "password":self.password, "firstname": self.firstname,
                "lastname": self.lastname, "token": self.token}

if __name__ == '__main__':
    from sqlalchemy import create_engine, engine

    engine = create_engine('mysql://root@localhost/hmpblv')
    Base.metadata.create_all(engine)

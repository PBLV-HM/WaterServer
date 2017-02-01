from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, PrimaryKeyConstraint, Float

Base = declarative_base()
class Device(Base):
    __tablename__ = 'Device'
    id = Column(String, primary_key=True, nullable=False)
    name = Column(String(50))
    username = Column('user', String, ForeignKey("User.username"))

    def __repr__(self):
        return "<id(id='%s', name='%s')>" % (self.id, self.name)



class GroupEntrie(Base):
    __tablename__ = 'Groups'
    grpID = Column('grpID', Integer, ForeignKey("Group.grpID"), nullable=False)
    devID = Column('devID', String, ForeignKey("Device.id"), nullable=False),
    timestamp = Column('timestamp', DateTime, nullable=False),
    normPeg = Column('normPeg', Float)
    PrimaryKeyConstraint('devID', 'timestamp')
    def __repr__(self):
        return "<Groups(grpID='%s', timestamp='%s', devID='%s')>" % (
                                self.grpID, self.timestamp, self.devID)

class Group(Base):
    __tablename__ = 'Group'
    grpName = Column('grpName', String, nullable=False)
    grpID = Column('grpID', Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Groups(grpID='%s', grpName='%s', devID='%s')>" % (
                                self.grpID, self.grpName)


class Data(Base):
    __tablename__ = 'Data'
    devID = Column('devID', String, nullable=False)
    timestamp = Column('timestamp', DateTime, nullable=False)
    PrimaryKeyConstraint('devID', 'timestamp')
    lon = Column('lon', Float)
    lat = Column('lat', Float)
    deg = Column('deg', Float)
    distance = Column('deg', Integer)

class User(Base):
    username = Column('username', String, primary_key=True, nullable=False)
    password = Column('password', String, nullable=False)
    token = Column('token', String)

    def __repr__(self):
        return "<Groups(grpID='%s', timestamp='%s', devID='%s')>" % (
                                self.grpID, self.timestamp, self.devID)


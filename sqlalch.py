from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, PrimaryKeyConstraint, Float, Boolean
from passlib.apps import custom_app_context as pwd_context

from flaskBase import db, app

Base = db.Model

class Device(Base):
    __tablename__ = 'Device'
    id = Column(String(32), primary_key=True, nullable=False)
    name = Column(String(50))
    active = Column(Boolean)
    userId = Column('userId', Integer)

    def __repr__(self):
        return {"userId": self.userId, "name": self.name, "active": self.active, "id": self.id}

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
    userId = Column('userId', Integer, ForeignKey("User.id"))

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
    password_hash = Column('password_hash', String(128), nullable=False)
    firstname = Column('firstname', String(32))
    lastname = Column('lastname', String(32))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user

    def __repr__(self):
        #return "<User(username='%s', password='%s', token='%s', firstname='%s', lastname='%s')>" % (
        #                        self.username, self.password, self.token, self.firstname, self.lastname)
        return {"id": self.id, "username":self.username, "password":self.password_hash, "firstname": self.firstname,
                "lastname": self.lastname}

if __name__ == '__main__':
    from sqlalchemy import create_engine, engine

    engine = create_engine('mysql://hmpblv:ahs7ThasaiMioj@localhost/hmpblv')
    Base.metadata.create_all(engine)

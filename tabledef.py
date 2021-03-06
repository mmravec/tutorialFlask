from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql+mysqlconnector://root:@localhost/test', echo=True)
Base = declarative_base()


########################################################################
class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(80))
    password = Column(VARCHAR(120))

    # ----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password


# create tables
Base.metadata.create_all(engine)
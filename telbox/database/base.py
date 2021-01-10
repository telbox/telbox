from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import Column, INTEGER, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
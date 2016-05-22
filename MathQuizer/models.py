from sqlalchemy import *
from sqlalchemy.orm import *
from splalchemy.sql import *
from databaseSetup import Base, User, Student
import datetime
import logging


engine = create_engine('postgresql://mqdbuser:mqpassword@localhost/mathquizerdb')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


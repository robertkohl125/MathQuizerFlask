from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import logging

Base = declarative_base()

#Builds the User table in the ORM
class User(Base):
    """Connects to the User table
    """
    __tablename__ = 'user'

    name =      Column(String(20))
    email =     Column(String(20))


#Builds the Student table in the ORM
class Student(Base):
    """Connects to the Student table
    """
    __tablename__ = 'student'

    name =      Column(String(20))
    email =     Column(String(20))
    rank =      Column(Integer, default = 0)


#Connect to a PostGreSQL database with the following parameters:
#   database:   mathquizerdb
#   user:       mqdbuser
#   password:   mqpassword
engine = create_engine('postgresql://mqdbuser:mqpassword@localhost/mathquizerdb')
Base.metadata.create_all(engine) 

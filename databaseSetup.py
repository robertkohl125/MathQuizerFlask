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

    user_id =    Column(Integer, primary_key = True)
    name =      Column(String(20), nullable = False)
    email =     Column(String(20))


#Builds the Student table in the ORM
class Student(Base):
    """Connects to the Student table
    """
    __tablename__ = 'student'

    student_id =    Column(Integer, primary_key = True)
    name =      Column(String(20), nullable = False)
    email =     Column(String(20))
    rank =      Column(Integer, default = 0)
    parent_id =    Column(Integer, ForeignKey('user.user_id'))


#Connect to a PostGreSQL database with the following parameters:
#   database:   mathquizerdb
#   user:       mqdbuser
#   password:   mqpassword
#engine = create_engine('postgresql://mqdbuser:mqpassword@localhost/mathquizerdb')
engine = create_engine('sqlite:///mathquizer.db')
Base.metadata.create_all(engine) 

"""
description

First, create a python virtual environment, set up SQLAlchemy and create a SQLAlchemy model for the table that will store the colors and their frequencies.

Establish a connection to your PostgreSQL database using SQLAlchemy.

Create a table in the database based on the SQLAlchemy model.

Insert the colors and frequencies into the table.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""Define the SQLAlchemy database connection, parameterd and URL"""
dbname = 'database_name'
user = 'database_user'
password = 'database_password'
host = 'database_host'
port = 'database_port'

db_url = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

"""Create a SQLAlchemy engine"""
engine = create_engine(db_url)

"""Define a SQLAlchemy Base"""
Base = declarative_base()

"""Define the SQLAlchemy model for the table"""
class ColorFrequency(Base):
    __tablename__ = 'color_frequencies'

    color = Column(String, primary_key=True)
    frequency = Column(Integer)

"""Create the table in the database"""
Base.metadata.create_all(engine)

"""Create a SQLAlchemy session"""
Session = sessionmaker(bind=engine)
session = Session()

""" import the colors and its frequency from mean then Define the colors and their frequencies"""
from mean import color_counts as colors_data
"""convert colors_data to a dictionary"""
color_data  = dict(colors_data)

"""Insert colors and frequencies into the table"""
for data in color_data:
    color_entry = ColorFrequency(**data)
    session.add(color_entry)

"""Commit the changes to the database"""
session.commit()

"""Close the session"""
session.close()

print("Colors and frequencies have been saved to the database using SQLAlchemy.")

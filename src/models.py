import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(20), nullable = False)
    email = Column(String(100), nullable = False)
    favorite = relationship('Favorite', backref='user')



class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    imagen = Column(String(100), nullable = True)
    description = Column(String(100), nullable = False)
    vehicle = relationship('Vehicles', backref='card')
    planet = relationship('Planets', backref='card')
    characters = relationship('Characters', backref='card')


class Planets(Base):
    __tablename__ = 'planets'
    name = Column(Integer, ForeignKey('card.name'))
    image = Column(Integer, ForeignKey('card.image'))
    description = Column(Integer, ForeignKey('card.description'))
    id = Column(Integer, primary_key = True)
    population = Column(String(100), nullable = False)
    climate = Column(String(100), nullable = False)
    rotate_period = Column(String(100), nullable = False)
    diameter = Column(String(100), nullable = False)
    orbital_period = Column(String(100), nullable = False)
    card = relationship('Card', backref = 'card')

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key = True)
    name = Column(Integer, ForeignKey('card.name'))
    image = Column(Integer, ForeignKey('card.image'))
    description = Column(Integer, ForeignKey('card.description'))
    model = Column(String(100), nullable = False)
    passagers = Column(String(100), nullable = False)
    lenght = Column(String(100), nullable = False)
    cargo_capacity = Column(String(100), nullable = False)
    consumables = Column(String(100), nullable = False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key = True)
    name = Column(Integer, ForeignKey('card.name'))
    image = Column(Integer, ForeignKey('card.image'))
    description = Column(Integer, ForeignKey('card.description'))
    eye_color = Column(String(100), nullable = False)
    skin_color = Column(String(100), nullable = False)
    birth_date = Column(String(100), nullable = False)
    gender = Column(String(100), nullable = False)
    height = Column(String(100), nullable = False)
    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, primary_key = True)
    card_id = Column(Integer, primary_key = True)
# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
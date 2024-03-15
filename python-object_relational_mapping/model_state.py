#!/usr/bin/python3
"""
Defines the class State and an instance Base using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

Base = declarative_base()

class State(Base):
    """
    The class definition of a State that inherits from Base.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
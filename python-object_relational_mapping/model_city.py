#!/usr/bin/python3
"""
Defines the City class which inherits from Base and
links to the MySQL table cities.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    The City class, defining attributes and linking to the 'cities' table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return "({}, '{}')".format(self.id, self.name)

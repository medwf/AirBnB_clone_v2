#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

TypeStorage = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if TypeStorage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade='all, delete')
    else:
        name = ""

    @property
    def cities(self):
        """returns the list of Cities"""
        from models.city import City
        from models.__init__ import storage
        List_cities = []
        ALLcities = storage.all(City)
        for city in ALLcities.value():
            if city.state_id == self.id:
                List_cities.append(city)
        return List_cities

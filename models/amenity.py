#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.place import place_amenity

TypeStorage = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """class Amenity"""
    __tablename__ = "amenities"

    if TypeStorage == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        name = ""

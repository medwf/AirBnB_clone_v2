#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

TypeStorage = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """class Amenity"""
    __tablename__ = "amenities"

    if TypeStorage == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary='place_amenity',
            back_populates="amenities")
    else:
        name = ""

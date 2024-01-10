#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import ValueEnv


class Amenity(BaseModel, Base):
    """class Amenity"""
    if ValueEnv == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary="place_amenity", back_populates="amenities")
    else:
        name = ""

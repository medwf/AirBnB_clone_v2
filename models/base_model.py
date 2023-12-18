#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from email.policy import default
from turtle import update
import uuid
from datetime import datetime
from venv import create
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,
                        Integer,
                        String,
                        datetime)
from models import storage

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new Base object.
        Args:
            args (won't be used): list of argumments.
            kwargs: pass in dictionary as argumment.
        """
        if kwargs:
            for attr, v in kwargs.items():
                # fix error: type of created_at and updated_at most be datetime
                if attr in ('created_at', 'updated_at'):
                    Nv = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, attr, Nv)
                elif attr != "__class__":
                    setattr(self, attr, v)
        else:
            id = Column(String(60), primary_key=True, nullable=False)
            create_at = Column(datetime, default=datetime.utcnow(), nullable=False)
            update_at = Column(datetime, default=datetime.utcnow(), nullable=False)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        for key, v in dictionary.items():
            if key == '_sa_instance_state':
                del(key)
        return dictionary
    
    def delete(self):
        key = 

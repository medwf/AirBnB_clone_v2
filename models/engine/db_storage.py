#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Session
from base_model import Base
import os

class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        db_name = os.environ.get("HBNB_MYSQL_DB")
        data_URL = f"mysql+mysqldb://{user}:{password}@{host}:3306/{db_name}"
        self.__engine = create_engine(data_URL, pool_pre_ping=True)
        is_equal = (os.environ.get("HBNB_ENV") == "test")
        if is_equal:
            metadata = MetaData()
            metadata.bind = self.__engine
            metadata.reflect()
            metadata.drop_all()
    def all(self, cls=None):
        self.__session = Session()
        result = None
        my_dict = {}
        inner_dict = {}
        if cls == None:
            result = self.__session.query(Base).all()
        else:
            result = self.__session.query(cls).all()
        for key in result:
            attribute_names = [attr for attr in vars(key) if not callable(getattr(key, attr))]
            key1 = f"{type(key).__name__}.{key.id}"
            i = 0
            my_dict[key1] = inner_dict[attribute_names[i]]
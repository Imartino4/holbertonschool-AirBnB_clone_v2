#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os


if os.getenv('HBNB_TYPE_STORAGE') == "file":
    storage = FileStorage()
    storage.reload()

else:
    storage = DBStorage()
    storage.reload()

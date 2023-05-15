#!/usr/bin/python3
"""__init__ method for model packages,
Module for FileStorage auto init."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

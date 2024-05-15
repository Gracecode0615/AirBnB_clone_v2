#!/usr/bin/python3
"""
storage - Creates an instance of FileStorage
storage.reload() - Reloads data
"""


from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()

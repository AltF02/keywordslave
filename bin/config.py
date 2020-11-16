"""
The reason why this file exists is to prevent any circular dependency errors
"""
from configparser import ConfigParser

conf = ConfigParser()
conf.read('conf.ini')

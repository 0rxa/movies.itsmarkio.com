import os

class Config:
    basedir = os.environ.get("PWD") + "/../"
    repos = [ 'movies' ]
    key = os.environ.get("SECRET")



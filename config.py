import os

basedir = os.path.abspath(os.path.dirname(__file__))
magic_key_word = "1207"


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "carlos_was_here"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "users.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

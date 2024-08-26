from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),nullable = False)
    _password_hash = db.Column(db.String(60), nullable = False)


    def __repr__(self):
        return f"User {self.id},  {self.username}"
    
    def set_password(self, password):
        self._password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self._password_hash, password) 
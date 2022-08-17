from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(70), unique=True)
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.Text)

    def __repr__(self):
        return '<Role %r>' % self.id

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Notes(db.Model, UserMixin):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    content = db.Column(db.Text)
    user_note = db.Column(db.Integer, db.ForeignKey('users.id'))


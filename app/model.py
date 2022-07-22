from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.Text)

    def __repr__(self):
        return '<Role %r>' % self.id

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



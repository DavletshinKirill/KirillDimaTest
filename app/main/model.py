# from .. import db
# from flask_login import UserMixin
#
#
# class Note(UserMixin, db.Model):
#     __tablename__ = 'notes'
#     note_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     title = db.Column(db.String(64))
#     content = db.Column(db.Text)
#
#     def __repr__(self):
#         return '<Role %r>' % self.id

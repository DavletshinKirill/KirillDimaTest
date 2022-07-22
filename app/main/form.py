from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length


class NoteForm(FlaskForm):
    title = StringField("Title Note", validators=[DataRequired(), Length(1, 30)])
    content = StringField("Content", validators=[DataRequired(), Length(20, 120)])
    submit = SubmitField("Add message")

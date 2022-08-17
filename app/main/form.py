from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class NoteForm(FlaskForm):
    title = StringField("Title Note", validators=[DataRequired(), Length(1, 20)])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    search = StringField("Title Note")

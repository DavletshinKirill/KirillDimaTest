from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired()])
    user_name = StringField("Name: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(1, 30)])
    check_password = PasswordField("Password: ", validators=[DataRequired(), Length(1, 30)])
    submit = SubmitField("Log In")

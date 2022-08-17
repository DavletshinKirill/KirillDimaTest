from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import *
from wtforms.validators import *

# это статика (choices_music), которую нужно вынести в отдельный файл
# разобрать как работает flask form на уровне представления и на уровне класса — Nope
# BOOTSTRAP — done
# почитать как пишутся макросы — done
# почитать про flask csv и mapping — done
# сверстать таблицу юзеров, где выводятся все юзеры — done
# кнопки crud сверху — done

choices_music = [('cpp', 'C++'),
                 ('py', 'Python'),
                 ('cl', 'C#')]


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


class NewForm(FlaskForm):
    boolean = BooleanField("BooleanField: ", validators=[DataRequired()])
    string = StringField("StringField: ", validators=[DataRequired()])
    text_area = TextAreaField("TextAreaField", validators=[DataRequired()])
    password = PasswordField("PasswordField: ", validators=[DataRequired(), Length(1, 30)])
    file = FileField("FileField", validators=[FileRequired()])
    date = DateField("DateField")
    radio = RadioField("RadioField", choices=choices_music)
    select = SelectField("SelectMultipleField", choices=choices_music)
    submit = SubmitField("Log In")

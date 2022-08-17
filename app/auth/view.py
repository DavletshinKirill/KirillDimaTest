from flask import render_template, flash, redirect, url_for, session, request, jsonify
from werkzeug.security import generate_password_hash
from .. import db
from app.model import Users
from .form import LoginForm, RegistrationForm, NewForm
from .. import login_manager
from flask_login import login_user, logout_user, login_required
from . import auth
from ..email import send_email


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@auth.route("/log in", methods=['GET', 'POST'])
def login(colour=True):
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=True)
            session.update({"username": user.email})
            return redirect(url_for("main.notes_storage"))
        else:
            flash("You entered incorrect email or password")
            colour = False
    return render_template("index.html", form=form, title="login", colour=colour)


@auth.route("/registration", methods=['GET', 'POST'])
def registration():
    colour = True
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data == form.check_password.data:
            user = create_user(form)
            if isinstance(user, str):
                flash(user)
                colour = False
            else:
                send_email(form.email.data.lower(), "Welcome", 'You have successfully registered')
                login_user(user, remember=True)
                session.update({"username": user.email})
                return redirect(url_for("main.notes_storage", username=user.email))
        else:
            flash("Your passwords isn't same")
            colour = False
    return render_template("index.html", form=form, title="registration", colour=colour)


@auth.route("/log out")
@login_required
def logout():
    session.pop("username")
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for("auth.login"))


@auth.route("/", methods=['GET', 'POST'])
def index():
    form = NewForm()
    if request.method == 'POST':
        json = request.json
        print(json)
        button = json["button"]
        return jsonify({"responce": " You pushed " + button})
    return render_template("index.html", form=form)


@auth.errorhandler(401)
def not_authorized(e):
    return redirect(url_for("auth.login"))


def create_user(form):
    if not check_email(form.email.data.lower()):
        return "You entered email which already exist"
    elif not check_name(form.user_name.data):
        return "You entered name which already exist"
    else:
        user = Users(email=form.email.data.lower(), user_name=form.user_name.data,
                     password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
    return user


def check_email(email):
    email = Users.query.filter_by(email=email).first()
    if email:
        return False
    return True


def check_name(name):
    name = Users.query.filter_by(user_name=name).first()
    if name:
        return False
    return True

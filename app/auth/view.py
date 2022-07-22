from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash
from .. import db
from app.model import Users
from .form import LoginForm, RegistrationForm
from .. import login_manager
from flask_login import login_user, logout_user, login_required
from . import auth
from ..email import send_email

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@auth.route("/log in", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=True)
        return redirect(url_for("auth.index"))
    else:
        flash("You entered incorrect email or password")
    return render_template("index.html", form=form)


@auth.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data == form.check_password.data:
            user = Users(email=form.email.data.lower(), user_name=form.user_name.data,
                         password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            send_email(form.email.data.lower(), "Welcome", 'You have successfully registered')
            login_user(user, remember=True)
            return render_template('base.html')
        else:
            flash("Nope (write smth else for this message)")
    return render_template("index.html", form=form)


@auth.route("/log out")
@login_required
def logout():
    form = LoginForm()
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for("login"))


@auth.route("/")
def index():
    return render_template("base.html")


@auth.errorhandler(404)
def page_not_found(e):
    return render_template('<h1>Page did not found</h1>')

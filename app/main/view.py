from . import main
from flask_login import login_required
from flask import render_template, flash
from .. import db

from .form import NoteForm


# @main.route("/main", methods=['GET', 'POST'])
# @login_required
# def index():
#     form = NoteForm()
#     if form.validate_on_submit():
#         user = Note(user_id=1, title=form.title, content=form.content)
#         db.session.add(user)
#         db.session.commit()
#         return render_template("base.html")
#     return render_template("index.html", form=form)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('<h1>Page did not found</h1>')

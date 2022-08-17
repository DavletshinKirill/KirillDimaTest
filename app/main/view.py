from . import main
from flask import url_for, redirect, session, render_template, request, make_response, jsonify
from flask_login import login_required
from .. import db
from ..model import Notes, Users
from .form import NoteForm, SearchForm

# все параметры пользователя передавать через session — done
# сделать стандартные макросы на editor и browser
# добавить Фильтр — done
# вынести кнопки — done
# сделать элементы таблицы выбираемыми — done
# login log out вынести вправо
# отступ слева и справа 1/10 экрана
# поискать updater для pycharm полный pycharm — done
# почитать про time datetime, научиться работать с базовыми операциями
# нотация большого О(ооо, не ноль)
# глобальные переменные flask
# сделать hot-keys
# продумать пример приложения, которое мы бы хотели бы сделать в качестве портфолио
# fetch plan
# стратегия добавления и удаления компонентов


@main.route("/main/table", methods=['GET', 'POST'])
@login_required
def notes_storage():
    notes = Notes.query.filter_by(user_note=Users.query.filter_by(email=session["username"]).first().id).all()
    form = SearchForm()
    # if request.method == 'POST':
    #     json = request.json
    #     print(json)
    #     button = json["button"]
    #     return jsonify({"responce": " You pushed " + button})
    # if request.method == 'POST':
    #     variable = request.json
    #     print(variable["button"])
    #     button = variable["button"]
        # if variable['search_button'] == "search_button":
        #     notes = Notes.query.filter_by(name=request.form.get("search")).all()
        # elif variable['button'] == "update":
        #     return redirect(url_for("main.update", name=variable['choice_item']))
        # elif variable['button'] == "delete":
        #     return redirect(url_for("main.delete", name=variable['choice_item']))
        # return jsonify({"responce": " You pushed " + button})
    return render_template("user.html", notes=notes,  title=session["username"], form=form)


@main.route("/main/table/<name>/update", methods=['GET', 'POST'])
@login_required
def update(name):
    note = Notes.query.filter_by(name=name).first()
    form = NoteForm()
    if form.validate_on_submit():
        note.name = form.title.data
        note.content = form.content.data
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("main.notes_storage"))
    form.title.data = note.name
    form.content.data = note.content
    return render_template("index.html", form=form, title=name)


@main.route("/main/table/<name>/delete", methods=['GET', 'POST'])
@login_required
def delete(name):
    note = Notes.query.filter_by(name=name).first()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("main.notes_storage"))


@main.route("/main/table/create", methods=['GET', 'POST'])
@login_required
def create():
    form = NoteForm()
    if form.validate_on_submit():
        note = Notes(name=form.title.data, content=form.content.data, user_note=Users.query.filter_by(email=session["username"]).first().id)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("main.notes_storage"))
    return render_template("index.html", form=form, title="Create Note")


@main.errorhandler(401)
def not_authorized(e):
    return redirect(url_for("auth.login"))


# @main.errorhandler(400)
# def user_error(e):
#     pass

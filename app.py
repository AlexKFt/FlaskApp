from werkzeug.utils import redirect

from io_handlers.flask_handler import FlaskIOHandler

from group import Group

from flask import Flask, request
from flask import render_template
from flask import g

from models_v2.director import Director
from models_v2.person import Person
from models_v2.worker import Worker

app = Flask(__name__)


@app.template_test('instanceof')
def is_instanceof(value, type_name):
    return value.__class__.__name__ == type_name

def GetGroup():
    if 'group' not in g:
        g.group = Group(io_handler=FlaskIOHandler())
    return g.group


@app.route("/")
def index():
    group = GetGroup()
    return render_template("group.tpl", group=group.get_items())


@app.route("/showform/<int:id>")
def show_form(id):
    group = GetGroup()
    if id == 1:
        person = Person(io_handler=group.io_handler)
        return render_template("person_form.tpl", person=person)
    elif id == 2:
        worker = Worker(io_handler=group.io_handler)
        return render_template("worker_form.tpl", person=worker)
    elif id == 3:
        director = Director(io_handler=group.io_handler)
        return render_template("director_form.tpl", person=director)
    else:
        return render_template("group.tpl", group=group.get_items())


@app.route("/edit/<int:id>")
def edit_item(id):
    group = GetGroup()
    person = group.get_item(id)
    if type(person) is Director:
        return render_template("director_form.tpl", person=person)
    elif type(person) is Worker:
        return render_template("worker_form.tpl", person=person)
    else:
        return render_template("person_form.tpl", person=person)

@app.route("/delete/<int:id>")
def delete_item(id):
    group = GetGroup()
    group.delete(id)
    return redirect("/")


@app.route("/add", methods=['POST'])
def add():

    type = request.form['obj_class']
    group = GetGroup()
    cls = group.classes.get(type)
    group.add(cls)

    return redirect("/")


@app.teardown_appcontext
def teardown_book(ctx):
    GetGroup().storage.store()

if __name__ == "__main__":
    app.run(debug=True)
import copy

from werkzeug.utils import redirect

from .storage.pickle_storage import PickleStorage
from .io_handlers.flask_handler import FlaskIOHandler

from .group import Group

from flask import render_template, Flask, request
from flask import g

from .models.student import Student
from .models.leader import Leader

app = Flask(__name__)


@app.template_test('instanceof')
def is_instanceof(value, type_name):
    return value.__class__.__name__ == type_name


def get_group():
    if 'group' not in g:
        g.group = Group(io_handler=FlaskIOHandler(request))
    return g.group


@app.route("/")
def index():
    group = get_group()
    group.show_items()
    return render_template("group.tpl", group=group.show_items())


@app.route("/showform/<int:id>")
def show_form(id):
    group = get_group()
    if id == 1:
        person = Student(io_handler=group.io_handler)
        return render_template("student_form.tpl", person=person)
    elif id == 2:
        worker = Leader(io_handler=group.io_handler)
        return render_template("leader_form.tpl", person=worker)
    else:
        return render_template("group.tpl", group=group.get_items())

@app.route("/edit_form/<int:cls_id>/<int:id>")
def edit_form(cls_id, id):
    group = get_group()
    person = group.get_item(id)
    if cls_id == 1:
        return render_template("student_form.tpl", person=person)
    elif cls_id == 2:
        return render_template("leader_form.tpl", person=person)
    else:
        return render_template("group.tpl", group=group.get_items())

@app.route("/edit", methods=['POST'])
def edit_item():
    id = int(request.form.get("id"))
    group = get_group()
    person = group.get_item(id)
    person.input()
    group.edit(person)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_item(id):
    group = get_group()
    group.delete(id)
    return redirect("/")


@app.route("/add", methods=['POST'])
def add():
    type = request.form['obj_class']
    group = get_group()
    cls = group.classes.get(type)
    group.add(cls)

    return redirect("/")

@app.route("/load_from_pickle")
def load_from_pickle():
    group = get_group()
    storage = PickleStorage(group)
    for item in storage.get_items():
        item.id = 0
        group.storage.add(item)
    return redirect("/")

@app.teardown_appcontext
def teardown_book(ctx):
    get_group().storage.store()
from io_handlers.flask_io import FlaskIO

from container import Group

from flask import Flask, request
from flask import render_template
from flask import g

app = Flask(__name__)


def GetGroup():
    if 'group' not in g:
        g.group = Group(io_strategy=None)
        g.flask_io = FlaskIO(g.group)
        g.group.io_strategy = g.flask_io
    return g.group


@app.route("/")
def index():
    group = GetGroup()
    return render_template("group.tpl", students=group.storage.GetItems())


@app.route("/showform/<int:id>")
def show_form(id):
    group = GetGroup()
    item = group.GetItem(id)
    item.set_io(group.io_strategy)
    return render_template("student_form.tpl", student=item)


@app.route("/delete/<int:id>")
def delete_item(id):
    group = GetGroup()
    group.Delete(id)
    return render_template("group.tpl", students=group.storage.GetItems())


@app.route("/add", methods=['POST'])
def add():
    type = request.form['obj_class']
    group = GetGroup()
    cls = group.classes.get(type)
    student = group.GetItem(int (request.form.get("id", 0)))

    student.set_io(group.io_strategy)
    student.io_strategy.data = request.form
    student.input()

    group.Add(student)
    return render_template("group.tpl", students=group.storage.GetItems())


@app.teardown_appcontext
def teardown_book(ctx):
    GetGroup().storage.Store()

if __name__ == "__main__":
    app.run(debug=True)
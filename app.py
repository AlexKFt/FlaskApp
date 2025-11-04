from io_handlers.flask_handler import FlaskIOHandler

from group import Group

from flask import Flask, request
from flask import render_template
from flask import g

app = Flask(__name__)


def GetGroup():
    if 'group' not in g:
        g.group = Group(io_handler=FlaskIOHandler())
    return g.group


@app.route("/")
def index():
    group = GetGroup()
    return render_template("group.tpl", students=group.get_items())


@app.route("/showform/<int:id>")
def show_form(id):
    group = GetGroup()
    item = group.get_item(id)
    item.set_io(group.io_handler)
    return render_template("student_form.tpl", student=item)


@app.route("/delete/<int:id>")
def delete_item(id):
    group = GetGroup()
    group.delete(id)
    return render_template("group.tpl", students=group.get_items())


@app.route("/add", methods=['POST'])
def add():
    type = request.form['obj_class']
    group = GetGroup()
    cls = group.classes.get(type)
    student = group.get_item(int (request.form.get("id", 0)))

    student.set_io(group.io_handler)
    student.io_strategy.data = request.form
    student.input()

    group.add(student)
    return render_template("group.tpl", students=group.get_items())


@app.teardown_appcontext
def teardown_book(ctx):
    GetGroup().storage.store()

if __name__ == "__main__":
    app.run(debug=True)
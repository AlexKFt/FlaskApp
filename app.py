import io
from dataclasses import dataclass
import os, sys, re, codecs, binascii, datetime, pickle

from werkzeug.utils import redirect

from io_handlers import flask_io
from io_handlers.flask_io import FlaskIO
from io_handlers.web_io import WebIO

from container import Group

from flask import Flask, url_for, request
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
    return GetGroup().io_strategy.render_index()


@app.route("/showform/<int:id>")
def show_form(id):
    return GetGroup().ShowItem(id)


@app.route("/delete/<int:id>")
def delete_item(id):
    GetGroup().Delete(id)
    return redirect(url_for("index"))


@app.route("/add", methods=['POST'])
def add():
    type = "1"
    group = GetGroup()
    student = group.classes.get(type)
    if student:
        student.name = request.form["name"];
        student.age = int(request.form["age"]);
        group.Add(student)
        return redirect(url_for("index"))


@app.teardown_appcontext
def teardown_book(ctx):
    GetGroup().storage.Store()

if __name__ == "__main__":
    app.run(debug=True)
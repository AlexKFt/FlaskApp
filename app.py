import io
from dataclasses import dataclass
import os, sys, re, codecs, binascii, datetime, pickle
from io_handlers.web_io import WebIO

from container import Group

from flask import Flask
from flask import render_template
from flask import g

app = Flask(__name__)

def GetGroup():
    if 'group' not in g:
        io_strategy = WebIO()
        g.group = Group(io_strategy)
    return g.group

@app.route("/")
def book_index():
    return GetGroup().ShowItems()

@app.route("/showform/<int:id>")
def show_form(id):
    return GetGroup().Show(id)

@app.route("/delete/<int:id>")
def delete_item(id):
    return GetGroup().Delete(id)

@app.route("/add", methods=['POST'])
def add():
    return GetGroup().Add()

@app.teardown_appcontext
def teardown_book(ctx):
    GetGroup().storage.Store()

if __name__ == "__main__":
    app.run(debug=True)
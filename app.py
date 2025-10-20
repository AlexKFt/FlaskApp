from dataclasses import dataclass
import os, sys, re, codecs, binascii, datetime, pickle

from container import Group

from flask import Flask
from flask import render_template
from flask import g

app = Flask(__name__)

def GetGroup():
    if 'book' not in g:
        g.group = Group()
    return g.book

@app.route("/")
def bookindex():
    return GetGroup().GetHeader() + GetGroup().ShowBook() + GetGroup().GetFooter()

@app.route("/showform/<int:id>")
def showform(id):
    return GetGroup().GetHeader() + GetGroup().ShowForm(id) + GetGroup().GetFooter()

@app.route("/delete/<int:id>")
def deleteitem(id):
    return GetGroup().GetHeader() + GetGroup().Delete(id) + GetGroup().GetFooter()

@app.route("/add", methods=['POST'])
def add():
    return GetGroup().GetHeader() + GetGroup().Add() + GetGroup().GetFooter()

@app.teardown_appcontext
def teardown_book(ctx):
    GetGroup().storage.Store()

if __name__ == "__main__":
    app.run(debug=True)
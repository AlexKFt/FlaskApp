from pickletools import read_uint1

from io_handlers.io_handler import IOHandler
from models_v2.director import Director
from models_v2.worker import Worker
from models_v2.person import Person
from flask import request


class FlaskIOHandler(IOHandler):
    def read(self, cls):
        data = request.form
        id = int(data.get("id"))
        name = data.get("name")
        age = int(data.get("age"))

        if cls is Worker:
            return Worker(name, age, data.get("position", ""), id=id, io_handler=self)
        elif cls is Director:
            return Director(name, age, data.get("department", ""), id=id, io_handler=self)
        else:
            return Person(name, age, id=id, io_handler=self)

    def write(self, obj):
        return f"<p>{obj}</p>"

    def info(self, message):
        return f"<p>info: {message}</p>"
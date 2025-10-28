from pickletools import read_uint1

from io_handlers.io_handler import IOHandler
from models_v2.Director import Director
from models_v2.Worker import Worker

class FlaskIOHandler(IOHandler):
    def read(self, cls):
        from flask import request
        data = request.form
        name = data.get("name")
        age = int(data.get("age"))

        if cls is Worker:
            return Worker(name, age, data.get("position", ""), io_handler=self)
        elif cls is Director:
            return Director(name, age, data.get("department", ""), io_handler=self)
        else:
            return "Неизвестный тип объекта."

    def write(self, obj):
        return f"<p>{obj}</p>"
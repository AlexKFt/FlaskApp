from io_handlers.io_handler import IOHandler

from flask import request


class FlaskIOHandler(IOHandler):
    def __init__(self):
        self.output = []

    def read(self, field):
        data = request.form
        return data.get(field, "")

    def write(self, title, value):
        self.output.append(f"<p>{title}: {value}</p>")

    def info(self, message):
        return f"<p>info: {message}</p>"

    def get_output(self):
        return "".join(self.output)
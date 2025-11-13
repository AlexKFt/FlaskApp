from app.io_handlers.io_handler import IOHandler


class FlaskIOHandler(IOHandler):
    def __init__(self, request):
        self.form = request.form
        self.output = []

    def read(self, field):
        return self.form.get(field, "")

    def write(self, title, value):
        self.output.append(f"<p>{title}: {value}</p>")

    def info(self, message):
        return f"<p>info: {message}</p>"

    def get_output(self):
        return "".join(self.output)
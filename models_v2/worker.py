from io_handlers.io_handler import IOHandler
from models_v2.person import Person


class Worker(Person):
    def __init__(self, name="", age=0, position="", io_handler=None):
        super().__init__(name, age, io_handler)
        self.position = position

    def show(self):
        return self.io_handler.write(self)

    def input(self):
        return self.io_handler.read(Worker)

    def __str__(self):
        return f"Worker(name={self.name}, age={self.age}, position={self.position})"
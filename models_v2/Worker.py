from io_handlers.io_handler import IOHandler
from models_v2.person import Person


class Worker(Person):
    def __init__(self, name, age, position, io_handler: IOHandler):
        super().__init__(name, age, io_handler)
        self.position = position

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age}, position={self.position})"
from io_handlers.io_handler import IOHandler
from models_v2.person import Person


class Director(Person):
    def __init__(self, name, age, department, io_handler: IOHandler):
        super().__init__(name, age, io_handler)
        self.department = department

    def __str__(self):
        return f"Boss(name={self.name}, age={self.age}, department={self.department})"
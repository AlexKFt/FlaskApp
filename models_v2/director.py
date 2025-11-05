from io_handlers.io_handler import IOHandler
from models_v2.person import Person


class Director(Person):
    def __init__(self, name="", age=0, department="", id=0, io_handler=None):
        super().__init__(name, age, io_handler, id)
        self.department = department

    def show(self):
        return self.io_handler.write(self)

    def input(self):
        director = self.io_handler.read(Director)
        if director.id == 0:
            director.id = self.id
        return director

    def __str__(self):
        return f"Director(name={self.name}, age={self.age}, department={self.department})"
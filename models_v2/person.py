from io_handlers.io_handler import IOHandler

class Person:
    def __init__(self, name="", age=0, io_handler=None):
        self.id = 0
        self.name = name
        self.age = age
        self.io_handler = io_handler

    def show(self):
        return self.io_handler.write(self)

    def input(self):
        return self.io_handler.read(Person)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
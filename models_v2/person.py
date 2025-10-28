from io_handlers.io_handler import IOHandler

class Person:
    def __init__(self, name, age, io_handler: IOHandler):
        self.id = 0
        self.name = name
        self.age = age
        self.io_handler = io_handler

    def save(self):
        return self.io_handler.write(self)

    @classmethod
    def load(cls, io_handler):
        return io_handler.read(cls)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
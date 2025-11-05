class Person:
    def __init__(self, name="", age=0, io_handler=None, id = 0):
        self.id = id
        self.name = name
        self.age = age
        self.io_handler = io_handler

    def show(self):
        return self.io_handler.write(self)

    def input(self):
        person = self.io_handler.read(Person)
        if person.id == 0:
            person.id = self.id
        return person

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
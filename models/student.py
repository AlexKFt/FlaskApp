
class Student:
    def __init__(self, id=0, name="", age=0, io_handler=None):
        self.id = id
        self.name = name
        self.age = age
        self.io_handler = io_handler

    def input(self):
        self.name = self.io_handler.read("name")
        self.age = int(self.io_handler.read("age"))

    def show(self):
        self.io_handler.write("Имя", self.name)
        self.io_handler.write("Возраст", self.age)

    def __str__(self):
        return f"Студент \nИмя:{self.name}\nВозраст:{self.age}"

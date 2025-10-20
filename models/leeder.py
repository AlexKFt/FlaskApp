from .student import Student

class Leeder(Student):
    def __init__(self, id=0, name="", age=0, group=""):
        super().__init__(id, name, age)
        self.group = group

    def set_io(self, io):
        super().set_io(io)

    def input(self):
        super().input()
        self.group = self.io_strategy.read("group")

    def print(self):
        super().print()
        self.io_strategy.write("group", self.group)


class Student:
    def __init__(self, id=0, name="", age=0):
        self.io_strategy = None
        self.id = id
        self.name = name
        self.age = age

    def set_io(self, strategy):
        self.io_strategy = strategy

    def validate_age(self, age_str):
        if not age_str.isdigit():
            return 18
        age = int(age_str)
        return age if 0 <= age <= 180 else 18

    def input(self):
        if not self.io_strategy:
            return

        self.name = self.io_strategy.read("name")
        self.age = self.validate_age(self.io_strategy.read("age"))

    def show(self):
        if self.io_strategy:
            self.io_strategy.write("id", self.id)
            self.io_strategy.write("name", self.name)
            self.io_strategy.write("age", self.age)

    def Show(self):
        return "Student profile edit"

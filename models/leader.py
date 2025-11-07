from models.student import Student


class Leader(Student):
    def __init__(self, id=0, name="", age=0, group="", io_handler=None):
        super().__init__(id, name, age, io_handler)
        self.group = group

    def input(self):
        super().input()
        self.group = self.io_handler.read("group")

    def show(self):
        super().show()
        self.io_handler.write("Группа", self.group)

    def __str__(self):
        return f"Староста \nИмя:{self.name}\nВозраст:{self.age}\nГрупп:{self.group}"

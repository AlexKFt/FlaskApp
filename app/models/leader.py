from app.models.student import Student


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

    def load(self, row):
        self.id = row['id']
        self.name = row['name']
        self.age = row['age']
        self.group = row['group_name']

    def store(self, db):
        if not self.id or int(self.id) == 0:
            db.execute("insert into students values(NULL, ?, ?, ?, ?)",
                       (self.age, self.name, self.group, self.__class__.__name__.lower()))
        else:
            db.execute("update students set age=?, name=?, group_name=?, type=? where id=?",
                       (self.age, self.name, self.group, self.__class__.__name__.lower(), self.id))

    def __str__(self):
        return f"Староста \nИмя:{self.name}\nВозраст:{self.age}\nГрупп:{self.group}"

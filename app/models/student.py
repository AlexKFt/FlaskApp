from dataclasses import dataclass

from app.io_handlers.io_handler import IOHandler


@dataclass
class Student:
    id: int = 0
    name: str = ""
    age: int = 0
    io_handler: IOHandler = None

    def input(self):
        self.name = self.io_handler.read("name")
        self.age = int(self.io_handler.read("age"))

    def output(self):
        self.io_handler.write("Id", self.id)
        self.io_handler.write("Имя", self.name)
        self.io_handler.write("Возраст", self.age)

    def load(self, row):
        self.id = row['id']
        self.name = row['name']
        self.age = row['age']

    def store(self, db):
        if not self.id or int(self.id) == 0:
            db.execute("insert into students values(NULL, ?, ?, ?, ?)",
                       (self.age, self.name, None, self.__class__.__name__.lower()))
        else:
            db.execute("update students set age=?, name=?, group_name=?, type=? where id=?",
                       (self.age, self.name, None, self.__class__.__name__.lower(), self.id))

    def __str__(self):
        return f"Студент \nИмя:{self.name}\nВозраст:{self.age}"

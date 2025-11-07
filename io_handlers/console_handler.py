from io_handlers.io_handler import IOHandler
from models_v2.director import Director
from models_v2.worker import Worker
from models_v2.person import Person


class ConsoleIOHandler(IOHandler):
    def read(self, cls):
        print(f"\nСоздание объекта {cls.__name__}")
        name = input("Имя: ")
        age = int(input("Возраст: "))

        if cls is Worker:
            position = input("Должность: ")
            return Worker(name, age, position, io_handler=self)
        elif cls is Director:
            department = input("Департамент: ")
            return Director(name, age, department, io_handler=self)
        else:
            return Person(name, age, io_handler=self)

    def write(self, obj):
        print(f"Id: {obj.id}")
        print(f"Имя: {obj.name}")
        print(f"Возраст: {obj.age}")

        if type(obj) is Worker:
            print(f"Должность: {obj.position}")
        elif type(obj) is Director:
            print(f"Департамент: {obj.department}")
        print('\n')


    def info(self, message):
        print(message)
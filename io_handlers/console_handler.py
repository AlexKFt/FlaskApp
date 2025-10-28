from io_handlers.io_handler import IOHandler
from models_v2.Director import Director
from models_v2.Worker import Worker


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
            return "Неизвестный тип объекта."
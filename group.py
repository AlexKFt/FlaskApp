import copy

from io_handlers.io_handler import IOHandler
from models.student import Student
from models.leader import Leader
from storage.pickle_storage import PickleStorage


class Group:
    def __init__(self, io_handler: IOHandler):
        self.storage = PickleStorage()
        self.io_handler = None
        self.set_io_handler(io_handler)
        self.classes = {
            "1": Student,
            "2": Leader
        }

    def set_io_handler(self, io_handler: IOHandler):
        self.io_handler = io_handler
        for item in self.storage.get_items():
            item.io_handler = copy.deepcopy(io_handler)

    def add(self, cls):
        person = cls(io_handler=self.io_handler)
        person.input()
        self.storage.add(person)

    def edit(self, person):
        self.storage.edit(person)

    def get_item(self, id):
        return self.storage.get_item(id)

    def delete(self, id):
        self.storage.delete(id)

    def get_items(self):
        return self.storage.get_items()

    def show_items(self):
        for item in self.storage.get_items():
            item.show()


    def save(self):
        self.storage.store()
        self.io_handler.info("Сохранено.")

    def load(self):
        try:
            self.storage.load()
            self.io_handler.info("Данные загружены.")
        except FileNotFoundError:
            self.io_handler.info("Ошибка чтения файла с данными")

    def clear(self):
        self.storage.clear()
        self.io_handler.info("Список очищен.")

    def __len__(self):
        return self.storage.size()
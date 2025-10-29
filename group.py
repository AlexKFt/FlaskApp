from io_handlers.io_handler import IOHandler
from models_v2.person import Person
from models_v2.worker import Worker
from models_v2.director import Director
from storage.pickle_storage import PickleStorage


class Group:
    def __init__(self, io_handler: IOHandler):
        self.storage = PickleStorage()
        self.io_handler = io_handler
        self.classes = {
            "1": Person,
            "2": Worker,
            "3": Director
        }

    def add(self, cls):
        person = cls(io_handler=self.io_handler)
        cls.input(cls)
        self.storage.add(person)

    def edit(self, person):
        self.storage.edit(person)

    def get_item(self, id):
        return self.storage.get_item(id)

    def delete(self, id):
        self.storage.delete(id)

    def get_items(self):
        self.storage.get_items()

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
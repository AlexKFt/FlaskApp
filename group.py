from io_handlers.io_handler import IOHandler
from models_v2.person import Person
from storage.pickle_storage import PickleStorage


class Company:
    def __init__(self, io_handler: IOHandler):
        self.storage = PickleStorage()
        self.people = {}
        self.maxid = 0
        self.io_handler = io_handler

    def Add(self, person):
        self.storage.Add(person)

    def CreateAndAdd(self, cls):
        obj = cls.load(self.io_handler)
        self.add(obj)

    def GetItem(self, id):
        return self.storage.GetItem(id)

    def Delete(self, id):
        self.storage.Delete(id)

    def GetItems(self):
        for (key, value) in self.people.items():
            yield value

    def Save(self):
        self.storage.Store()
        self.io_handler.info("Сохранено.")

    def Load(self):
        try:
            self.storage.Load()
            self.io_handler.info("Данные загружены.")
        except FileNotFoundError:
            self.io_handler.info("Ошибка чтения файла с данными")

    def Clear(self):
        self.storage.Clear()
        self.io_handler.info("Список очищен.")

    def __len__(self):
        return len(self.people)
from models.leeder import Leeder, Student
from io_handlers.console_io import ConsoleIO
from storage.pickle_storage import PickleStorage

class Group:
    def __init__(self, io_strategy):
        self.io_strategy = io_strategy
        self.storage = PickleStorage()
        self.classes = {
            "1": Student,
            "2": Leeder
        }

    def Add(self, type):
        """
        Добавляе объект в соотвтествии с кодом типа
        type: 1 - Студент, 2 - Староста
        """
        cls = self.classes.get(type)
        if cls:
            student = cls()
            student.set_io(self.io_strategy)
            student.input()
            self.storage.Add(student)

    def ShowItems(self):
        if not self.storage.items:
            self.io_strategy.info("Список пуст.")
        for item in self.storage.GetItems():
            item.Show()

    def ShowItem(self, id):
        item = self.storage.GetItem(id)
        item.Show()

    def Delete(self, id):
        self.storage.Delete(id)

    def Edit(self, id):
        item = self.storage.GetItem(id)
        if item:
            item.input()

    def Save(self):
        self.storage.Store()
        self.io_strategy.info("Сохранено.")

    def Load(self):
        try:
            self.storage.Load()
            self.io_strategy.info("Загружено.")
        except FileNotFoundError:
            self.io_strategy.info("Файл не найден.")

    def Clear(self):
        self.storage.Clear()
        self.io_strategy.info("Список очищен.")
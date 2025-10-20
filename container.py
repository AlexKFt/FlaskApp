from models.leeder import Leeder, Student
from io_handlers.console_io import ConsoleIO
from storage.pickle_storage import PickleStorage

class Group:
    def __init__(self):
        self.students = list()
        self.io_strategy = ConsoleIO()
        self.storage_strategy = PickleStorage()
        self.classes = {
            "1": Student,
            "2": Leeder
        }

    def add(self):
        print("Выберите тип объекта: 1 - Студент, 2 - Староста")
        choice = input("Ваш выбор: ")
        cls = self.classes.get(choice)
        if cls:
            student = cls()
            student.set_io(self.io_strategy)
            student.input()
            self.students.append(student)
            print("Объект добавлен.")
        else:
            print("Неверный выбор.")

    def show_items(self):
        if not self.students:
            print("Список пуст.")
        for i, student in enumerate(self.students, 1):
            print(f"{i})", end=' ')
            student.print()

    def delete_item(self):
        self.show_items()
        idx = int(input("Введите номер объекта для удаления: ")) - 1
        if 0 <= idx < len(self.students):
            del self.students[idx]
            print("Удалено.")
        else:
            print("Ошибка индекса.")

    def edit_item(self):
        self.show_items()
        idx = int(input("Введите номер объекта для редактирования: ")) - 1
        if 0 <= idx < len(self.students):
            self.students[idx].input()
            print("Объект изменен.")
        else:
            print("Ошибка индекса.")

    def save_to_file(self):
        self.storage_strategy.save(self.students)
        print("Сохранено.")

    def load_from_file(self):
        try:
            self.students = self.storage_strategy.load()
            print("Загружено.")
        except FileNotFoundError:
            print("Файл не найден.")

    def clear_items(self):
        self.students.clear()
        print("Список очищен.")
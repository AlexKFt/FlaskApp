from group import Group
from io_handlers.console_handler import ConsoleIOHandler



def main():
    group = Group(ConsoleIOHandler())

    def add_item():
        for type, value in group.classes.items():
            print(f"{type}: {value}")
        id = input("Выберите тип: ")
        if id in group.classes:
            cls = group.classes[id]
            group.add(cls)
        else:
            print("Введено некорректное значение")

    menu = {
        "1": add_item,
        "2": group.edit,
        "3": group.delete,
        "4": group.get_items,
        "5": group.save,
        "6": group.load,
        "7": group.clear,
        "0": exit,
    }

    while True:
        print("\nМеню:")
        print("1 - Добавить объект")
        print("2 - Редактировать объект")
        print("3 - Удалить объект")
        print("4 - Показать список")
        print("5 - Сохранить в файл")
        print("6 - Загрузить из файла")
        print("7 - Очистить список")
        print("0 - Выход")

        choice = input("Выберите действие: ")
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()

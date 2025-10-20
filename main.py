from container import Group

def main():
    c = Group()
    menu = {
        "1": c.Add,
        "2": c.Edit(),
        "3": c.Delete(),
        "4": c.ShowItems(),
        "5": c.Save(),
        "6": c.Load(),
        "7": c.Clear(),
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

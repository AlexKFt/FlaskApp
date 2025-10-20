from container import Group

def main():
    c = Group()
    menu = {
        "1": c.add,
        "2": c.edit_item,
        "3": c.delete_item,
        "4": c.show_items,
        "5": c.save_to_file,
        "6": c.load_from_file,
        "7": c.clear_items,
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

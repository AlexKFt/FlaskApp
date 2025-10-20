

class ConsoleIO:
    def read(self, field_name: str):
        return input(f"{field_name}: ")

    def write(self, title: str, value: str):
        print(f"{title}: {value}")

    def info(self, message: str):
        print(message)
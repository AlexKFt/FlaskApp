

class ConsoleIO:
    def read(self, field):
        return input(f"{field}: ")

    def write(self, title, value):
        print(f"{title}: {value}")
from io_handlers.io_handler import IOHandler
from models.leeder import Leeder


class ConsoleIO:
    def read(self, field_name: str):
        return input(f"{field_name}: ")

    def write(self, field_name: str, value: str):
        print(f"{field_name}: {value}")

    def info(self, message: str):
        print(message)


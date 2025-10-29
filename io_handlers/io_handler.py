from abc import ABC, abstractmethod

class IOHandler(ABC):
    @abstractmethod
    def read(self, cls):
        pass

    @abstractmethod
    def write(self, value):
        pass

    def info(self, message):
        pass
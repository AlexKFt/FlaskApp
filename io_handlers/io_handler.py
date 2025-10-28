from abc import ABC, abstractmethod

class IOHandler(ABC):
    @abstractmethod
    def read(self, cls):
        pass

    @abstractmethod
    def write(self, cls):
        pass

    def info(self, cls):
        pass
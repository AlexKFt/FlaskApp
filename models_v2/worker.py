from models_v2.person import Person


class Worker(Person):
    def __init__(self, name="", age=0, position="", id=0, io_handler=None):
        super().__init__(name, age, io_handler, id)
        self.position = position

    def show(self):
        return self.io_handler.write(self)

    def input(self):
        worker = self.io_handler.read(Worker)
        if worker.id == 0:
            worker.id = self.id
        return worker

    def __str__(self):
        return f"Worker(name={self.name}, age={self.age}, position={self.position})"
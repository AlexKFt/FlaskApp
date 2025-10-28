from io_handlers.io_handler import IOHandler
from models_v2.person import Person


class Company:
    def __init__(self, io_handler: IOHandler):
        self.people = {}
        self.maxid = 0
        self.io_handler = io_handler

    def add(self, person):
        if person.id <= 0:
            self.maxid += 1
            person.id = self.maxid
            self.people[self.maxid] = person

    def create_and_add(self, cls):
        obj = cls.load(self.io_handler)
        self.add(obj)

    def get_item(self, id):
        if id in self.people:
            return self.people[id]
        else:
            return None

    def get_items(self):
        for (key, value) in self.people.items():
            yield value

    def __len__(self):
        return len(self.people)
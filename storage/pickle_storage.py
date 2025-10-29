import pickle
from models.student import Student

class PickleStorage:
    def __init__(self):
        try:
            self.Load()
        except:
            self.items = {}
            self.maxid = 0

    def store(self):
        with open("data.dat", "wb") as f:
            pickle.dump((self.maxid, self.items), f)

    def load(self):
        with open("data.dat", "rb") as f:
            (self.maxid, self.items) = pickle.load(f)
            print(self.maxid)

    def get_item(self, id):
        if id in self.items:
            return self.items[id]
        else:
            return None

    def add(self, item):
        if item.id <= 0:
            self.maxid += 1
            item.id = self.maxid
            self.items[self.maxid] = item

    def edit(self, item):
        if item.id in self.items:
            self.items[item.id] = item

    def delete(self, id):
        if id in self.items:
            del self.items[id]

    def get_items(self):
        for (id, item) in self.items.items():
            yield item

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = {}
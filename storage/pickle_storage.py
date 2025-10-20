import pickle
from container import Group, Student

class PickleStorage:
    def __init__(self, group):
        self.group = group
        try:
            self.Load()
        except:
            self.items = {}
            self.maxid = 0

    def Store(self, data):
        with open("data.dat", "wb") as f:
            pickle.dump((self.maxid, self.items), f)

    def Load(self):
        with open("data.dat", "rb") as f:
            (self.maxid, self.items) = pickle.load(f)

    def GetItem(self, id):
        if id <= 0:
            return Student()
        else:
            return self.items[id]

    def Add(self, item):
        self.maxid += 1
        self.items[self.maxid] = item

    def Delete(self, id):
        del self.items[id]

    def GetItems(self):
        for (id, item) in self.items.items():
            yield item

    def Clear(self):
        self.items = {}
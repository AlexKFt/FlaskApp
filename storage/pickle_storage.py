import pickle
from models.student import Student

class PickleStorage:
    def __init__(self):
        try:
            self.Load()
        except:
            self.items = {}
            self.maxid = 0

    def Store(self):
        with open("data.dat", "wb") as f:
            pickle.dump((self.maxid, self.items), f)

    def Load(self):
        with open("data.dat", "rb") as f:
            (self.maxid, self.items) = pickle.load(f)
            print(self.maxid)

    def GetItem(self, id):
        if id <= 0:
            return Student()
        else:
            return self.items[id]

    def Add(self, item):
        if item.id <= 0:
            self.maxid += 1
            item.id = self.maxid
            self.items[self.maxid] = item

    def Delete(self, id):
        if id in self.items:
            del self.items[id]

    def GetItems(self):
        for (id, item) in self.items.items():
            yield item

    def Clear(self):
        self.items = {}
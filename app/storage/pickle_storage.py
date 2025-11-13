import pickle

bin_path = 'data/pickle/'

class PickleStorage:
    def __init__(self, group):
        try:
            self.load()
        except:
            self.items = {}
            self.maxid = 0

    def store(self):
        with open(bin_path+"data.dat", "wb") as f:
            pickle.dump((self.maxid, self.items), f)

    def load(self):
        with open(bin_path+"data.dat", "rb") as f:
            (self.maxid, self.items) = pickle.load(f)

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
        elif item.id in self.items:
            self.items[item.id] = item

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
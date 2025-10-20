import pickle


class PickleStorage:
    def save(self, data):
        pickle.dump(data, open("data.dat", "wb"))

    def load(self):
        return pickle.load(open("data.dat", "rb"))
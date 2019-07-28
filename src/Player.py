class Player(object):
    def __init__(self, name):
        self.name = name
        self.history = []

    def print_history(self):
        print(self.name, self.history)

    def record(self, action):
        self.history.append(action)

class Action(object):
    @staticmethod
    def put(x, y, position):
        return "put: (%d, %d, %s)" % (x, y, position.piece.name)

    @staticmethod
    def move(x1, y1, x2, y2):
        return "move: from (%d, %d) to (%d, %d)" % (x1, y1, x2, y2)

    @staticmethod
    def eat(x, y):
        return "eat: (%d, %d)" % (x, y)

    @staticmethod
    def see(x, y):
        return "sea: (%d, %d)" % (x, y)

    @staticmethod
    def nums():
        return "nums"

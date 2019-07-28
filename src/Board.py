from collections import Counter


class Board(object):
    def __init__(self, type):
        if type == "chess":
            self.board = [[None for _ in range(8)] for _ in range(8)]
        if type == "go":
            self.board = [[None for _ in range(17)] for _ in range(17)]

    def is_valid(self, x, y):
        if x < len(self.board) and y < len(self.board):
            return
        raise Exception("({x}, {y}) 位置不合法！")

    def see(self, x, y):
        self.is_valid(x, y)

        return self.board[x][y]

    def put(self, x, y, position):
        self.is_valid(x, y)

        self.board[x][y] = position

    def move(self, x1, y1, x2, y2):
        self.is_valid(x1, y1)
        self.is_valid(x2, y2)

        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = None

    def eat(self, x, y):
        self.is_valid(x, y)

        self.board[x][y] = None

    def nums(self):
        nums = Counter()

        for line in self.board:
            for p in line:
                if p is None:
                    continue
                nums[p.player.name] += 1

        return nums

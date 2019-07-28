class Game(object):
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def print_history(self):
        self.player1.print_history()
        self.player2.print_history()


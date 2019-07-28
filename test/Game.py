import unittest

from src.Action import Action
from src.Board import Board
from src.Game import Game
from src.Piece import Piece
from src.Player import Player
from src.Position import Position


class Test(unittest.TestCase):
    def setUp(self):
        self.game = Game(Player("a"), Player("b"), Board("go"))
        self.game.player1.record(Action.put(1, 1, Position(Piece("a"), Player("a"))))
        self.game.player1.record(Action.see(1, 1))

    def test_print_history(self):
        self.game.print_history()


if __name__ == '__main__':
    unittest.main()

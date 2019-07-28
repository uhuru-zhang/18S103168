import unittest

from src.Action import Action
from src.Piece import Piece
from src.Player import Player
from src.Position import Position


class Test(unittest.TestCase):
    def setUp(self):
        self.player = Player("player")
        self.player.history.append(Action.put(1, 1, Position(Piece("a"), Player("a"))))
        self.player.history.append(Action.put(1, 2, Position(Piece("a"), Player("a"))))
        self.player.history.append(Action.see(1, 1))

    def test_print_history(self):
        self.player.print_history()


if __name__ == '__main__':
    unittest.main()

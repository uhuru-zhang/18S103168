import unittest

from src.Action import Action
from src.Piece import Piece
from src.Player import Player
from src.Position import Position

class Test(unittest.TestCase):
    def test_put(self):
        self.assertEqual(Action.put(1, 1, Position(Piece("a"), Player("a"))), "put: (%d, %d, %s)" % (1, 1, "a"))

    def test_move(self):
        self.assertEqual(Action.move(1, 1, 2, 2), "move: from (1, 1) to (2, 2)")

    def eat(self):
        self.assertEqual(Action.eat(1, 2), "eat: (%d, %d)" % (1, 1))

    def see(self):
        self.assertEqual(Action.see(1, 1), "sea: (%d, %d)" % (1, 1))

    def nums(self):
        self.assertEqual(Action.nums(), "nums")

if __name__ == '__main__':
    unittest.main()
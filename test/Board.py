import unittest
from collections import Counter

from src.Board import Board
from src.Piece import Piece


class Test(unittest.TestCase):
    def setUp(self):
        self.board = Board("go")
        self.board.put(1, 1, Piece("white"))

    def test_is_valid(self):
        self.assertRaises(self.board.is_valid(100, 100))
        self.assertRaises(self.board.is_valid(1, 1))

    def test_move(self):
        self.board.move(1, 1, 2, 2)
        self.board.move(0, 0, 2, 2)
        self.assertRaises(self.board.move(1, 1, 10, 100))

    def test_eat(self):
        self.board.eat(1, 1)
        self.assertRaises(self.board.eat(10, 100))

    def see(self):
        self.board.see(1, 1)
        self.assertRaises(self.board.see(10, 100))

    def nums(self):
        self.board.nums()


if __name__ == '__main__':
    unittest.main()

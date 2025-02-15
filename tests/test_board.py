import unittest

from board.board import Board
from board.field import Field
from constants import BOARD_LAYOUT, FIELD_IMAGES, ARROW_IMAGES, ARROW_LAYOUT


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_initialization(self):
        self.assertEqual(len(self.board.board), len(BOARD_LAYOUT))
        for row in self.board.board:
            self.assertEqual(len(row), len(BOARD_LAYOUT))

    def test_create_board(self):
        for i in range(len(BOARD_LAYOUT)):
            for j in range(len(BOARD_LAYOUT)):
                field = self.board.board[i][j]
                self.assertIsInstance(field, Field)
                self.assertEqual(field.field_type, BOARD_LAYOUT[i][j])
                self.assertEqual(field.image, FIELD_IMAGES.get(BOARD_LAYOUT[i][j], None))
                self.assertEqual(field.arrow_directions, ARROW_LAYOUT[i][j])
                self.assertEqual(field.arrow_images,
                                 [ARROW_IMAGES.get(direction, None) for direction in ARROW_LAYOUT[i][j]])


if __name__ == "__main__":
    unittest.main()

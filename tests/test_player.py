import unittest
from unittest.mock import patch

import pygame

from board.board import Board
from constants import TILE_SIZE, PLAYER_COLORS, PLAYER_RADIUS, ARROW_LAYOUT
from game.player import Player
from utils.renderer import Renderer


class TestPlayer(unittest.TestCase):

    def setUp(self):
        """Initialize pygame"""
        pygame.init()
        self.screen = pygame.Surface((400, 400))
        self.board = Board()
        self.renderer = Renderer(self.screen)

    def tearDown(self):
        """Quit pygame"""
        pygame.quit()

    def test_initialization(self):
        """Test if a Player is initialized"""
        player = Player(2, 3, 0)
        self.assertEqual(player.row, 2)
        self.assertEqual(player.col, 3)
        self.assertEqual(player.color, PLAYER_COLORS[0])
        self.assertEqual(player.money, 1000)
        self.assertEqual(player.possible_moves, [])

    def test_find_possible_moves_multiple_paths(self):
        """Test if multiple paths are found"""
        original_arrow_layout = [row[:] for row in ARROW_LAYOUT]
        try:

            ARROW_LAYOUT[0][0] = ["right", "down"]
            board = Board()
            player = Player(0, 0, 0)
            dice_result = 2
            player.find_possible_moves(board, dice_result)
            for move in player.possible_moves:
                self.assertEqual(len(move[2]), 3)
        finally:
            for i in range(len(ARROW_LAYOUT)):
                ARROW_LAYOUT[i] = original_arrow_layout[i]

    def test_money_methods(self):
        """Test if money can be spent and earned"""
        player = Player(0, 0, 0)
        player.spend_money(200)
        self.assertEqual(player.money, 800)
        player.earn_money(150)
        self.assertEqual(player.money, 950)

    def test_is_winner(self):
        """Test if a player wins when they run out of money."""
        player = Player(0, 0, 0)
        self.assertFalse(player.is_winner())
        player.spend_money(1000)
        self.assertTrue(player.is_winner())
        player.earn_money(-100)
        self.assertTrue(player.is_winner())

    @patch.object(Player, 'animate_path')
    def test_move_to(self, mock_animate_path):
        """Test if the player moves"""
        player = Player(0, 0, 0)
        player.possible_moves = [(1, 2, [(0, 0), (1, 2)])]
        player.move_to(1, 2, self.screen, self.renderer)
        mock_animate_path.assert_called_once_with(self.screen, self.renderer, [(0, 0), (1, 2)])
        self.assertEqual((player.row, player.col), (1, 2))
        self.assertEqual(player.possible_moves, [])

    @patch("pygame.draw.circle")
    def test_draw(self, mock_draw_circle):
        """Test if the player is drawn correctly"""
        player = Player(1, 2, 0)
        player.draw(self.screen)
        x_expected = player.col * TILE_SIZE + TILE_SIZE // 2
        y_expected = player.row * TILE_SIZE + TILE_SIZE // 2
        mock_draw_circle.assert_called_once_with(self.screen, player.color, (x_expected, y_expected), PLAYER_RADIUS)


if __name__ == "__main__":
    unittest.main()

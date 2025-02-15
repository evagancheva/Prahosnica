import unittest
from unittest.mock import Mock, patch

import pygame

from utils.renderer import Renderer


class TestRenderer(unittest.TestCase):
    def setUp(self):
        """Initialize Pygame"""
        pygame.init()
        self.screen = pygame.Surface((800, 600))
        self.renderer = Renderer(self.screen)

    def test_update_state(self):
        """Test if renderer update variables correctly"""
        board_mock = Mock()
        players_mock = [Mock(), Mock()]
        current_player_mock = 0
        dice_mock = Mock()
        self.renderer.update_state(board_mock, players_mock, current_player_mock, dice_mock)

        self.assertEqual(self.renderer._board, board_mock)
        self.assertEqual(self.renderer._players, players_mock)
        self.assertEqual(self.renderer._current_player, current_player_mock)
        self.assertEqual(self.renderer._dice, dice_mock)

    @patch("pygame.image.load")
    def test_get_image_caching(self, mock_load):
        """Test image cache"""
        mock_load.return_value = pygame.Surface((100, 100))
        image_path = "test_image.png"
        size = 50

        img1 = self.renderer.get_image(image_path, size)
        img2 = self.renderer.get_image(image_path, size)

        self.assertEqual(img1, img2)
        mock_load.assert_called_once_with(image_path)

    @patch.object(Renderer, "draw_image")
    def test_draw_arrows(self, mock_draw_image):
        """Test arrow drawing"""
        field_mock = Mock()
        field_mock.arrow_directions = ["up"]
        field_mock.arrow_images = ["arrow_up.png"]

        self.renderer.draw_arrows(field_mock, 100, 100)

        mock_draw_image.assert_called_once()

    @patch.object(Renderer, "draw")
    @patch.object(Renderer, "highlight_possible_moves")
    @patch.object(Renderer, "render_info_panel")
    def test_draw_game(self, mock_render_info, mock_highlight_moves, mock_draw):
        """Test if the game is drawn"""
        player_mock = Mock()
        player_mock.possible_moves = [(1, 1, None)]
        self.renderer._players = [player_mock]
        self.renderer._current_player = 0
        self.renderer._dice = Mock()

        self.renderer.draw_game()

        mock_draw.assert_called_once()
        mock_highlight_moves.assert_called_once()
        mock_render_info.assert_called_once()

    def test_disable(self):
        """Test disable function"""
        self.renderer._curr_flash_card = Mock()
        self.renderer.disable()
        self.assertIsNone(self.renderer._curr_flash_card)

    def tearDown(self):
        """Quit pygame"""
        pygame.quit()


if __name__ == "__main__":
    unittest.main()

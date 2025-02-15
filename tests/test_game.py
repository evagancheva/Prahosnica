import unittest
from unittest.mock import MagicMock, patch

from game.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        sound_patcher = patch('pygame.mixer.Sound', return_value=MagicMock())
        sound_patcher.start()
        self.addCleanup(sound_patcher.stop)

        num_players_patcher = patch.object(Game, "_choose_num_players", return_value=2)
        num_players_patcher.start()
        self.addCleanup(num_players_patcher.stop)
        self.mock_screen = MagicMock()
        self.game = Game(self.mock_screen)

        self.game._renderer.show_flash_card = MagicMock()
        self.game._renderer.update_state = MagicMock()
        self.game._renderer.draw_game = MagicMock()
        self.game._renderer.update = MagicMock()
        self.game._dice.roll = MagicMock()

        for player in self.game._players:
            player.find_possible_moves = MagicMock()
            player.move_to = MagicMock()

    def test_dice_roll_called(self):
        self.game._rolling_dice = False
        self.game._handle_dice_click()
        self.assertTrue(self.game._rolling_dice)
        self.game._dice.roll.assert_called_once_with(self.mock_screen)

    def test_field_effect_winner(self):
        player = self.game._players[0]
        player.is_winner = MagicMock(return_value=True)
        self.game.handle_field_effect(player)
        self.game._renderer.show_flash_card.assert_called_once()
        self.assertFalse(self.game._running)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import Mock, patch

from board.field import Field
from constants import FIELD_COSTS, PURPLE
from game.player import Player


class TestField(unittest.TestCase):
    def setUp(self):
        """Set up a mock renderer and a player"""
        self.mock_renderer = Mock()
        self.player = Player(start_row=0, start_col=0, player_id=0)

    def test_field_initialization(self):
        """Test if a Field is initialized"""
        field = Field("shop", "shop.png", "arrow.png", "up")
        self.assertEqual(field.field_type, "shop")
        self.assertEqual(field.image, "shop.png")
        self.assertEqual(field.arrow_images, "arrow.png")
        self.assertEqual(field.arrow_directions, "up")

    def test_apply_effect_purchase(self):
        """Test effect for purchase"""
        field_type = list(FIELD_COSTS.keys())[0]
        cost = FIELD_COSTS[field_type]
        field = Field(field_type, "test.png")

        initial_money = self.player.money
        field.apply_effect(self.player, self.mock_renderer)

        self.assertEqual(self.player.money, initial_money - cost)
        expected_message = f"Player {self.player.id + 1} buy a {field_type} for {cost}"
        self.mock_renderer.show_flash_card.assert_called_with("Purchase", expected_message, PURPLE)

    def test_apply_effect_flash_card_smiley(self):
        """Test smiley card"""
        field = Field("smiley", "smiley.png")
        initial_money = self.player.money
        with patch("random.randint", return_value=50):
            field.apply_effect(self.player, self.mock_renderer)
        self.assertEqual(self.player.money, initial_money - 50)
        self.mock_renderer.show_flash_card.assert_called()

    def test_apply_effect_flash_card_mad(self):
        """Test mad card"""
        field = Field("mad", "mad.png")
        initial_money = self.player.money
        with patch("random.randint", return_value=30):
            field.apply_effect(self.player, self.mock_renderer)
        self.assertEqual(self.player.money, initial_money + 30)
        self.mock_renderer.show_flash_card.assert_called()

    def test_apply_effect_flash_card_neutral(self):
        """Test neutral card"""
        field = Field("neutral", "neutral.png")

        initial_money = self.player.money
        with patch("random.choice", return_value=True), patch("random.randint", return_value=40):
            field.apply_effect(self.player, self.mock_renderer)
            self.assertEqual(self.player.money, initial_money - 40)

        self.player.money = initial_money
        with patch("random.choice", return_value=False), patch("random.randint", return_value=60):
            field.apply_effect(self.player, self.mock_renderer)
            self.assertEqual(self.player.money, initial_money + 60)

        self.mock_renderer.show_flash_card.assert_called()


if __name__ == "__main__":
    unittest.main()

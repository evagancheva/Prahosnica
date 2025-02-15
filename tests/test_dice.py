import unittest
from unittest.mock import patch, MagicMock

import pygame

from constants import DICE_MIN, DICE_MAX, DICE_IMAGES, DICE_ROLL_FRAMES, DICE_SIZE, DICE_X, DICE_Y
from game.dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        """Set up the test environment for Dice"""
        pygame.init()
        self.screen = pygame.Surface((640, 480))
        self.mixer_init_patcher = patch('pygame.mixer.init')
        self.mock_mixer_init = self.mixer_init_patcher.start()
        self.addCleanup(self.mixer_init_patcher.stop)
        self.sound_patcher = patch('pygame.mixer.Sound')
        self.mock_sound_class = self.sound_patcher.start()
        self.addCleanup(self.sound_patcher.stop)
        self.mock_sound_instance = MagicMock()
        self.mock_sound_class.return_value = self.mock_sound_instance

        self.dice = Dice()

    def test_roll_sets_value_and_calls_methods(self):
        """Test that rolling the dice updates its value and calls animation and draw methods"""
        with (patch('random.randint', return_value=4) as mock_randint, patch.object(self.dice, '_animate_roll')
        as mock_animate_roll, patch.object(self.dice, 'draw') as mock_draw):
            self.dice.roll(self.screen)
            mock_animate_roll.assert_called_once_with(self.screen)
            mock_randint.assert_called_once_with(DICE_MIN, DICE_MAX)
            mock_draw.assert_called_once_with(self.screen)
            self.assertEqual(self.dice.value, 4)

    def test_get_image_caches_images(self):
        """Test that the Dice class caches images"""
        dummy_surface = pygame.Surface((DICE_SIZE, DICE_SIZE))

        with patch('pygame.image.load', return_value=dummy_surface) as mock_load, patch('pygame.transform.scale',
                                                                                        return_value=dummy_surface) as mock_scale:
            image1 = self.dice._get_image("dummy_path.png", DICE_SIZE)
            image2 = self.dice._get_image("dummy_path.png", DICE_SIZE)
            mock_load.assert_called_once_with("dummy_path.png")
            self.assertIs(image1, image2)

    def test_draw_does_not_draw_when_no_value(self):
        """Test that draw() does nothing if the dice has no rolled value"""
        self.dice._value = None
        with patch.object(self.dice, '_get_image') as mock_get_image:
            self.dice.draw(self.screen)
            mock_get_image.assert_not_called()

    def test_draw_draws_correct_image_when_value_set(self):
        """Test if draw() get correct image"""
        self.dice._value = DICE_MIN
        dummy_surface = pygame.Surface((DICE_SIZE, DICE_SIZE))

        with patch.object(self.dice, '_get_image', return_value=dummy_surface) as mock_get_image:
            mock_screen = MagicMock()
            self.dice.draw(mock_screen)
            expected_image_path = DICE_IMAGES[DICE_MIN]
            mock_get_image.assert_called_once_with(expected_image_path, DICE_SIZE)
            mock_screen.blit.assert_called_once_with(dummy_surface, (DICE_X, DICE_Y))

    def test_animate_roll_plays_sound_and_draws_frames(self):
        """Test dice rolling animation sound and picture drawing """
        dummy_surface = pygame.Surface((DICE_SIZE, DICE_SIZE))
        with patch.object(self.dice, '_get_image', return_value=dummy_surface) as mock_get_image, patch(
                'pygame.draw.rect') as mock_draw_rect, patch('pygame.display.flip') as mock_flip, patch(
            'pygame.time.delay') as mock_delay:
            self.dice._animate_roll(self.screen)
            self.mock_sound_instance.play.assert_called_once()
            self.assertEqual(mock_get_image.call_count, len(DICE_ROLL_FRAMES))
            self.assertTrue(mock_draw_rect.called)
            self.assertTrue(mock_flip.called)
            self.assertTrue(mock_delay.called)

    def tearDown(self):
        pygame.quit()


if __name__ == '__main__':
    unittest.main()

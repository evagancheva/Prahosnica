import random

import pygame

from constants import (DICE_MIN, DICE_MAX, DICE_IMAGES, DICE_ROLL_FRAMES, DICE_ROLL_SOUND, DICE_SIZE, DICE_X, DICE_Y,
                       DARK_GREY)


class Dice:
    def __init__(self):
        self._value = None
        pygame.mixer.init()
        self._roll_sound = pygame.mixer.Sound(DICE_ROLL_SOUND)
        self._image_cache = {}

    @property
    def value(self):
        return self._value

    def roll(self, screen):
        self._animate_roll(screen)
        self._value = random.randint(DICE_MIN, DICE_MAX)
        self.draw(screen)

    def _get_image(self, image_path, size):
        if (image_path, size) not in self._image_cache:
            img = pygame.image.load(image_path)
            self._image_cache[(image_path, size)] = pygame.transform.scale(img, (size, size))
        return self._image_cache[(image_path, size)]

    def _animate_roll(self, screen):
        self._roll_sound.play()
        for frame in DICE_ROLL_FRAMES:
            img = self._get_image(frame, DICE_SIZE)
            pygame.draw.rect(screen, DARK_GREY, (DICE_X, DICE_Y, DICE_SIZE, DICE_SIZE))
            screen.blit(img, (DICE_X, DICE_Y))
            pygame.display.flip()
            pygame.time.delay(100)

    def draw(self, screen):
        if self._value:
            img = self._get_image(DICE_IMAGES[self._value], DICE_SIZE)
            screen.blit(img, (DICE_X, DICE_Y))

import random

import pygame

from constants import (DICE_MIN, DICE_MAX, DICE_IMAGES, DICE_ROLL_FRAMES, DICE_ROLL_SOUND, DICE_SIZE, DICE_X, DICE_Y,
                       DARK_GREY)


class Dice:
    def __init__(self):
        self.value = None
        pygame.mixer.init()
        self.roll_sound = pygame.mixer.Sound(DICE_ROLL_SOUND)

    def roll(self, screen):
        self.animate_roll(screen)
        self.value = random.randint(DICE_MIN, DICE_MAX)
        self.draw(screen)
        pygame.display.flip()

    def animate_roll(self, screen):
        self.roll_sound.play()
        for frame in DICE_ROLL_FRAMES:
            img = pygame.image.load(frame)
            img = pygame.transform.scale(img, (DICE_SIZE, DICE_SIZE))
            pygame.draw.rect(screen, DARK_GREY, (DICE_X, DICE_Y, DICE_SIZE, DICE_SIZE))
            screen.blit(img, (DICE_X, DICE_Y))
            pygame.display.flip()
            pygame.time.delay(100)

    def draw(self, screen):
        if self.value:
            img = pygame.image.load(DICE_IMAGES[self.value])
            img = pygame.transform.scale(img, (DICE_SIZE, DICE_SIZE))
            screen.blit(img, (DICE_X, DICE_Y))

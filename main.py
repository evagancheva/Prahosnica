import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.game import Game


def main():
    """Initialize pygame and window, run game"""
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(f"Prahosnica {FPS}fps")

    game = Game(window)
    game.run()


if __name__ == "__main__":
    main()

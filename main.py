import pygame

from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
from game.game import run, handle_events, draw_game

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"Прахосница {FPS}fps")


def main():
    clock = pygame.time.Clock()
    board, players, dice, current_player, rolling_dice = run(window)

    running = True
    while running:
        running, rolling_dice, current_player = handle_events(window, players, current_player, rolling_dice,
                                                              board, dice)

        draw_game(window, board, players, current_player, dice)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

import pygame

from board.board import Board
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BEIGE, DARK_GREY, FPS, TILE_SIZE, INFO_PANEL_WIDTH, BOARD_WIDTH
from utils.renderer import render_board

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"Прахосница {FPS}fps")


def main():
    clock = pygame.time.Clock()
    board = Board()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill(BEIGE)
        pygame.draw.rect(window, DARK_GREY, (BOARD_WIDTH, 0, INFO_PANEL_WIDTH, SCREEN_HEIGHT))

        render_board(window, board, TILE_SIZE)
        # render info panel logic ->money, player turn
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

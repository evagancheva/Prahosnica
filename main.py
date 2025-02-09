import pygame

from board.board import Board
from board.player import Player
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, BEIGE, DARK_GREY, FPS, TILE_SIZE, SPECIAL_TILES, INFO_PANEL_WIDTH,
                       INFO_PANEL_X)
from utils.renderer import draw_board, highlight_possible_moves, render_ui

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"Прахосница {FPS}fps")


def initialize_game():
    board = Board()
    players = [Player(row, col, i) for i, (row, col) in enumerate(SPECIAL_TILES.keys())]
    return board, players, 0, None, False  # (board, players, current_player, dice_result, rolling_dice)


def handle_events(players, current_player, rolling_dice, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, rolling_dice, None, current_player
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rolling_dice, dice_result, current_player = process_click(players, current_player, rolling_dice, board)
            return True, rolling_dice, dice_result, current_player
    return True, rolling_dice, None, current_player


def process_click(players, current_player, rolling_dice, board):
    x, y = pygame.mouse.get_pos()
    dice_result = None
    if x > INFO_PANEL_X:
        if not rolling_dice:
            rolling_dice = True
            dice_result = players[current_player].roll_dice()
            players[current_player].find_possible_moves(board)
        return rolling_dice, dice_result, current_player

    else:
        col, row = x // TILE_SIZE, y // TILE_SIZE
        if (row, col) in players[current_player].possible_moves:
            players[current_player].move_to(row, col)
            current_player = (current_player + 1) % len(players)
            rolling_dice = False
        return rolling_dice, None, current_player


def draw_game(window, board, players, current_player, dice_result):
    window.fill(BEIGE)
    pygame.draw.rect(window, DARK_GREY, (INFO_PANEL_X, 0, INFO_PANEL_WIDTH, SCREEN_HEIGHT))

    draw_board(window, board)
    for player in players:
        player.draw(window)

    highlight_possible_moves(window, players[current_player].possible_moves)
    render_ui(window, current_player, dice_result)
    pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    board, players, current_player, dice_result, rolling_dice = initialize_game()

    running = True
    while running:
        running, rolling_dice, new_dice_result, current_player = handle_events(players, current_player, rolling_dice,
                                                                               board)
        if new_dice_result is not None:
            dice_result = new_dice_result

        draw_game(window, board, players, current_player, dice_result)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

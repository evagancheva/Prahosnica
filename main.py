import pygame

from board.board import Board
from board.player import Player
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, BEIGE, DARK_GREY, FPS, TILE_SIZE, SPECIAL_TILES, INFO_PANEL_WIDTH,
                       INFO_PANEL_X, WHITE)
from utils.renderer import draw_board, highlight_possible_moves, render_ui

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(f"Прахосница {FPS}fps")

def choose_num_players(window):
    pygame.font.init()
    font = pygame.font.Font(None, 50)
    options = [2, 3, 4]

    while True:
        window.fill(DARK_GREY)
        text = font.render("Choose players count:", True, WHITE)
        window.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 100))

        buttons = []
        for i, num in enumerate(options):
            btn_x = SCREEN_WIDTH // 2 - 50
            btn_y = 200 + i * 80
            btn_rect = pygame.Rect(btn_x, btn_y, 100, 60)
            pygame.draw.rect(window, BEIGE, btn_rect)
            text = font.render(str(num), True, DARK_GREY)
            window.blit(text, (btn_x + 35, btn_y + 15))
            buttons.append((btn_rect, num))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for btn_rect, num in buttons:
                    if btn_rect.collidepoint(event.pos):
                        return num

def initialize_game():
    num_players = choose_num_players(window)
    board = Board()
    start_positions = list(SPECIAL_TILES.keys())[:num_players]
    players = [Player(row, col, i) for i, (row, col) in enumerate(start_positions)]
    return board, players, 0, None, False


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

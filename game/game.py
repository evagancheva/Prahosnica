import pygame

from board.board import Board
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, BEIGE, DARK_GREY, TILE_SIZE, SPECIAL_TILES, INFO_PANEL_WIDTH,
                       INFO_PANEL_X, WHITE, FONT_SIZE, TEXT_Y, BUTTON_SPACING, BUTTON_X, BUTTON_WIDTH, BUTTON_HEIGHT,
                       TEXT_OFFSET_Y, TEXT_X)
from game.dice import Dice
from game.player import Player
from utils.renderer import draw_board, highlight_possible_moves, render_ui


def choose_num_players(screen):
    pygame.font.init()
    font = pygame.font.Font(None, FONT_SIZE)
    options = [2, 3, 4]

    while True:
        screen.fill(DARK_GREY)
        text = font.render("Choose players count:", True, WHITE)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, TEXT_Y))

        buttons = []
        for i, num in enumerate(options):
            but_y = 200 + i * BUTTON_SPACING
            but_rect = pygame.Rect(BUTTON_X, but_y, BUTTON_WIDTH, BUTTON_HEIGHT)
            pygame.draw.rect(screen, BEIGE, but_rect)
            text = font.render(str(num), True, DARK_GREY)
            screen.blit(text, (TEXT_X, but_y + TEXT_OFFSET_Y))
            buttons.append((but_rect, num))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for but_rect, num in buttons:
                    if but_rect.collidepoint(event.pos):
                        return num


def draw_game(screen, board, players, current_player, dice):
    screen.fill(BEIGE)
    pygame.draw.rect(screen, DARK_GREY, (INFO_PANEL_X, 0, INFO_PANEL_WIDTH, SCREEN_HEIGHT))

    draw_board(screen, board)
    for player in players:
        player.draw(screen)

    highlight_possible_moves(screen, players[current_player].possible_moves)
    render_ui(screen, current_player, dice)
    dice.draw(screen)
    pygame.display.flip()


def process_click(screen, players, current_player, rolling_dice, board, dice):
    x, y = pygame.mouse.get_pos()
    if x > INFO_PANEL_X:
        if not rolling_dice:
            rolling_dice = True
            dice.roll(screen)
            players[current_player].find_possible_moves(board, dice.value)
        return rolling_dice, current_player

    else:
        col, row = x // TILE_SIZE, y // TILE_SIZE
        if (row, col) in players[current_player].possible_moves:
            players[current_player].move_to(row, col)
            current_player = (current_player + 1) % len(players)
            rolling_dice = False
        return rolling_dice, current_player


def handle_events(screen, players, current_player, rolling_dice, board, dice):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, rolling_dice, current_player
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rolling_dice, current_player = process_click(screen, players, current_player, rolling_dice, board, dice)
            return True, rolling_dice, current_player
    return True, rolling_dice, current_player


def run(screen):
    num_players = choose_num_players(screen)
    board = Board()
    dice = Dice()
    start_positions = list(SPECIAL_TILES.keys())[:num_players]
    players = [Player(row, col, i) for i, (row, col) in enumerate(start_positions)]
    return board, players, dice, 0, False

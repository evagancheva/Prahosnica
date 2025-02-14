import pygame
import pygame_menu

from board.board import Board
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, START_TILES, INFO_PANEL_X, FPS, GREEN)
from game.dice import Dice
from game.player import Player
from utils.renderer import Renderer


class Game:
    def __init__(self, screen):
        self._screen = screen
        self._board = Board()
        self._dice = Dice()
        self._renderer = Renderer(screen)
        self._num_players = self._choose_num_players()
        self._players = self._initialize_players()
        self._current_player = 0
        self._rolling_dice = False
        self._running = True

    def _choose_num_players(self):
        menu = pygame_menu.Menu("Welcome to Prahosnica", SCREEN_WIDTH, SCREEN_HEIGHT,
                                theme=pygame_menu.themes.THEME_BLUE)
        menu.add.label("Choose number of players:", font_size=30)
        drop_select = menu.add.dropselect(title="", items=[("2", 2), ("3", 3), ("4", 4)], default=0)
        menu.add.button('Start', menu.disable)
        menu.add.button('Exit', pygame_menu.events.EXIT)
        menu.mainloop(self._screen)

        return drop_select.get_value()[0][1]

    def _initialize_players(self):
        start_positions = list(START_TILES.keys())[:self._num_players]
        players = []
        for i, (row, col) in enumerate(start_positions):
            players.append(Player(row, col, i))
        return players

    def handle_field_effect(self, player):
        field = self._board.board[player.row][player.col]
        field.apply_effect(player, self._renderer)
        if player.is_winner():
            self._renderer.show_flash_card("", f"Player {player.id} win!", GREEN)
            self._running = False

    def _handle_dice_click(self):
        if not self._rolling_dice:
            self._rolling_dice = True
            self._dice.roll(self._screen)
            self._players[self._current_player].find_possible_moves(self._board, self._dice.value)

    def _handle_board_click(self, x, y):
        col, row = x // TILE_SIZE, y // TILE_SIZE
        player = self._players[self._current_player]

        if (row, col) in [move[:2] for move in player.possible_moves]:
            player.move_to(row, col, self._screen,self._renderer)
            self.handle_field_effect(player)

            if self._dice.value != 6:
                self._current_player = (self._current_player + 1) % len(self._players)
                self._renderer.update_state(self._board, self._players, self._current_player, self._dice)

            self._rolling_dice = False

    def process_click(self):
        x, y = pygame.mouse.get_pos()

        if x > INFO_PANEL_X:
            self._handle_dice_click()
        else:
            self._handle_board_click(x, y)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.process_click()

    def run(self):
        clock = pygame.time.Clock()
        self._renderer.update_state(self._board, self._players, self._current_player, self._dice)
        while self._running:
            self._renderer.update()
            self.handle_events()
            self._renderer.draw_game()
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()

import pygame
import pygame_menu

from board.board import Board
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, BEIGE, DARK_GREY, TILE_SIZE, START_TILES, INFO_PANEL_WIDTH,
                       INFO_PANEL_X, FPS, GREEN)
from game.dice import Dice
from game.player import Player
from utils.renderer import Renderer


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board()
        self.dice = Dice()
        self.renderer = Renderer(screen)
        self.num_players = self.choose_num_players()
        self.players = self.initialize_players()
        self.current_player = 0
        self.rolling_dice = False
        self.running = True

    def choose_num_players(self):
        menu = pygame_menu.Menu("Welcome to Prahosnica", SCREEN_WIDTH, SCREEN_HEIGHT,
                                theme=pygame_menu.themes.THEME_BLUE)
        menu.add.label("Choose number of players:", font_size=30)
        drop_select = menu.add.dropselect(title="", items=[("2", 2), ("3", 3), ("4", 4)], default=0)
        menu.add.button('Start', menu.disable)
        menu.add.button('Exit', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

        return drop_select.get_value()[0][1]

    def initialize_players(self):
        start_positions = list(START_TILES.keys())[:self.num_players]
        players = []
        for i, (row, col) in enumerate(start_positions):
            players.append(Player(row, col, i))
        return players

    def draw_game(self):
        self.screen.fill(BEIGE)
        pygame.draw.rect(self.screen, DARK_GREY, (INFO_PANEL_X, 0, INFO_PANEL_WIDTH, SCREEN_HEIGHT))

        self.renderer.draw(self.board)
        for player in self.players:
            player.draw(self.screen)

        self.renderer.highlight_possible_moves(self.players[self.current_player].possible_moves)
        self.renderer.render_info_panel(self.players, self.players[self.current_player], self.dice)

        if self.renderer.curr_flash_card:
            self.renderer.curr_flash_card.draw(self.screen)
        self.dice.draw(self.screen)

    def handle_field_effect(self, player):
        field = self.board.board[player.row][player.col]
        field.apply_effect(player, self.renderer)
        if player.is_winner():
            self.renderer.show_flash_card("",f"Player {player.id} win!", GREEN)
            self.running = False

    def process_click(self):
        x, y = pygame.mouse.get_pos()
        if x > INFO_PANEL_X:
            if not self.rolling_dice:
                self.rolling_dice = True
                self.dice.roll(self.screen)
                self.players[self.current_player].find_possible_moves(self.board, self.dice.value)
            return

        col, row = x // TILE_SIZE, y // TILE_SIZE
        player = self.players[self.current_player]

        if (row, col) in player.possible_moves:
            player.move_to(row, col)
            self.handle_field_effect(player)
            if self.dice.value != 6:
                self.current_player = (self.current_player + 1) % len(self.players)
            self.rolling_dice = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.process_click()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.renderer.update()
            self.handle_events()
            self.draw_game()
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()

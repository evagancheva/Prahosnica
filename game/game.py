import pygame

from board.board import Board
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, BEIGE, DARK_GREY, TILE_SIZE, START_TILES, INFO_PANEL_WIDTH,
                       INFO_PANEL_X, WHITE, FONT_SIZE, TEXT_Y, BUTTON_SPACING, BUTTON_X, BUTTON_WIDTH, BUTTON_HEIGHT,
                       TEXT_OFFSET_Y, TEXT_X, FPS)
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
        # da go napravq s pygame menu-> da e po-adekvatno
        pygame.font.init()
        font = pygame.font.Font(None, FONT_SIZE)
        options = [2, 3, 4]

        while True:
            self.screen.fill(DARK_GREY)
            text = font.render("Choose players count:", True, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, TEXT_Y))

            buttons = []
            for i, num in enumerate(options):
                but_y = 200 + i * BUTTON_SPACING
                but_rect = pygame.Rect(BUTTON_X, but_y, BUTTON_WIDTH, BUTTON_HEIGHT)
                pygame.draw.rect(self.screen, BEIGE, but_rect)
                text = font.render(str(num), True, DARK_GREY)
                self.screen.blit(text, (TEXT_X, but_y + TEXT_OFFSET_Y))
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

    def initialize_players(self):
        start_positions = list(START_TILES.keys())[:self.num_players]
        players = []
        for i, (row, col) in enumerate(start_positions):
            players.append(Player(row, col, i))
        return players

    def draw_game(self):
        self.screen.fill(BEIGE)
        pygame.draw.rect(self.screen, DARK_GREY, (INFO_PANEL_X, 0, INFO_PANEL_WIDTH, SCREEN_HEIGHT))

        self.renderer.draw_board(self.board)
        for player in self.players:
            player.draw(self.screen)

        self.renderer.highlight_possible_moves(self.players[self.current_player].possible_moves)
        self.renderer.render_ui(self.players, self.players[self.current_player], self.dice)
        self.dice.draw(self.screen)
        pygame.display.flip()

    def handle_field_effect(self, player):
        field = self.board.board[player.row][player.col]
        field.apply_effect(player, self.renderer)
        if player.is_winner():
            # da dobavq neshto za pobeda
            print(f"Player {player.id} win!")
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
            self.handle_events()
            self.draw_game()
            clock.tick(FPS)

        pygame.quit()

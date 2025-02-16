import pygame
import pygame_menu

from constants import (BLACK, GRID_WIDTH, MIDDLE_IMAGE, START_TILES, NO_GRID_TILES, ARROW_SIZE, ARROW_OFFSET,
                       INFO_PANEL_WIDTH, BOARD_WIDTH, INFO_PANEL_X, FONT_SIZE, PLAYER_COLORS, TILE_SIZE,
                       HIGHLIGHT_COLOR, SCREEN_HEIGHT, WHITE, FLASH_CARD_WIDTH, FLASH_CARD_HEIGHT, DARK_GREY, BEIGE,
                       FONT_SIZE_FLASH_CARDS)

pygame.font.init()
FONT = pygame.font.Font(None, FONT_SIZE)


class Renderer:
    def __init__(self, screen):
        """Initialize Renderer object"""
        self._screen = screen
        self._board = None
        self._players = []
        self._current_player = 0
        self._dice = None
        self._image_cache = {}
        self._curr_flash_card = None

    def update_state(self, board, players, current_player, dice):
        """Update some of Renderer class variables"""
        self._board = board
        self._players = players
        self._current_player = current_player
        self._dice = dice

    def get_image(self, image_path, size):
        """Load and cache images"""
        if (image_path, size) not in self._image_cache:
            img = pygame.image.load(image_path)
            self._image_cache[(image_path, size)] = pygame.transform.scale(img, (size, size))
        return self._image_cache[(image_path, size)]

    def draw_image(self, image_path, x, y, size):
        """Visualize image from path"""
        self._screen.blit(self.get_image(image_path, size), (x, y))

    def draw_arrows(self, field, x, y):
        """Visualize arrows from matrix"""
        for i in range(len(field.arrow_directions)):
            direction = field.arrow_directions[i]
            arrow_img_path = field.arrow_images[i]
            if arrow_img_path:
                arrow_x = x + TILE_SIZE // 2 + ARROW_OFFSET[direction][0] - ARROW_SIZE // 2
                arrow_y = y + TILE_SIZE // 2 + ARROW_OFFSET[direction][1] - ARROW_SIZE // 2
                self.draw_image(arrow_img_path, arrow_x, arrow_y, ARROW_SIZE)

    def update(self):
        """Update flash card"""
        if self._curr_flash_card:
            self._curr_flash_card.update(pygame.event.get())

    def draw(self):
        """Visualize the whole board"""
        for row_index, row in enumerate(self._board.board):
            for col_index, field in enumerate(row):
                x_position, y_position = col_index * TILE_SIZE, row_index * TILE_SIZE

                if 3 <= row_index <= 6 and 3 <= col_index <= 6:
                    continue

                if (row_index, col_index) in START_TILES:
                    pygame.draw.rect(self._screen, START_TILES[(row_index, col_index)],
                                     (x_position, y_position, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(self._screen, BLACK, (x_position, y_position, TILE_SIZE, TILE_SIZE),
                                     GRID_WIDTH)

                if field.image and (row_index, col_index) not in NO_GRID_TILES:
                    pygame.draw.rect(self._screen, BLACK, (x_position, y_position, TILE_SIZE, TILE_SIZE),
                                     GRID_WIDTH)
                    self.draw_image(field.image, x_position + TILE_SIZE // 5, y_position + TILE_SIZE // 5,
                                    int(TILE_SIZE * 0.6))

                if field.arrow_images:
                    self.draw_arrows(field, x_position, y_position)

        self.draw_image(MIDDLE_IMAGE, 3 * TILE_SIZE, 3 * TILE_SIZE, TILE_SIZE * 4)

    def draw_game(self):
        """Visualize the game - board, info panel and some special events"""
        self._screen.fill(BEIGE)
        pygame.draw.rect(self._screen, DARK_GREY, (INFO_PANEL_X, 0, INFO_PANEL_WIDTH, SCREEN_HEIGHT))
        self.draw()

        for player in self._players:
            player.draw(self._screen)

        self.highlight_possible_moves(self._players[self._current_player].possible_moves)

        self.render_info_panel(self._players, self._players[self._current_player], self._dice)
        if self._curr_flash_card:
            self._curr_flash_card.draw(self._screen)

        self._dice.draw(self._screen)

    def highlight_possible_moves(self, possible_moves):
        """Highlight all possible moves from current to position + dice value"""
        for row, col, _ in possible_moves:
            x, y = col * TILE_SIZE, row * TILE_SIZE
            pygame.draw.rect(self._screen, HIGHLIGHT_COLOR, (x, y, TILE_SIZE, TILE_SIZE), 3)

    def disable(self):
        """Stop flash card"""
        self._curr_flash_card = None

    def show_flash_card(self, card_type, text, color):
        """Visualize flash card"""
        if not self._curr_flash_card:
            curr_theme = pygame_menu.Theme(background_color=color, title_background_color=BLACK,
                                           title_font=pygame_menu.font.FONT_COMIC_NEUE, title_font_color=WHITE,
                                           widget_font_color=BLACK)
            flash_menu = pygame_menu.Menu(title=f"{card_type}", width=FLASH_CARD_WIDTH, height=FLASH_CARD_HEIGHT,
                                          theme=curr_theme)
            flash_menu.add.label(text, font_size=FONT_SIZE_FLASH_CARDS, max_char=30, font_color=BLACK)
            flash_menu.add.button("OK", lambda: self.disable())
            flash_menu.set_relative_position(28, 50)
            self._curr_flash_card = flash_menu

    def render_all_players_money(self, players):
        """Visualize players money in info panel"""
        money_title = FONT.render("Player Balances:", True, WHITE)
        self._screen.blit(money_title, (INFO_PANEL_X + 10, SCREEN_HEIGHT - 300))

        y_offset = SCREEN_HEIGHT - 260
        for player in players:
            money_text = FONT.render(f"Player {player.id + 1}: {player.money} ", True, player.color)
            self._screen.blit(money_text, (INFO_PANEL_X + 10, y_offset))
            y_offset += 40

    def render_info_panel(self, players, curr_player, dice):
        """Visualize info panel"""
        pygame.draw.rect(self._screen, DARK_GREY, (INFO_PANEL_X, 0, INFO_PANEL_WIDTH, BOARD_WIDTH))

        player_text = FONT.render(f"Player {curr_player.id + 1}", True, PLAYER_COLORS[curr_player.id])
        self._screen.blit(player_text, (INFO_PANEL_X + 50, 50))

        dice.draw(self._screen)

        instructions = FONT.render("Click to Roll", True, WHITE)
        self._screen.blit(instructions, (INFO_PANEL_X + 50, 250))
        self.render_all_players_money(players)

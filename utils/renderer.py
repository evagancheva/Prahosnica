import pygame
import pygame_menu

from constants import (BLACK, GRID_WIDTH, MIDDLE_IMAGE, START_TILES, NO_GRID_TILES, ARROW_SIZE, ARROW_OFFSET,
                       INFO_PANEL_WIDTH, BOARD_WIDTH, INFO_PANEL_X, FONT_SIZE, PLAYER_COLORS, TILE_SIZE,
                       HIGHLIGHT_COLOR, SCREEN_HEIGHT, WHITE, FLASH_CARD_WIDTH, FLASH_CARD_HEIGHT)

pygame.font.init()
FONT = pygame.font.Font(None, FONT_SIZE)


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.image_cache = {}

    def get_image(self, image_path, size):
        if (image_path, size) not in self.image_cache:
            img = pygame.image.load(image_path)
            self.image_cache[(image_path, size)] = pygame.transform.scale(img, (size, size))
        return self.image_cache[(image_path, size)]

    def draw_image(self, image_path, x, y, size):
        self.screen.blit(self.get_image(image_path, size), (x, y))

    def draw_arrows(self, field, x, y):
        for i in range(len(field.arrow_directions)):
            direction = field.arrow_directions[i]
            arrow_img_path = field.arrow_images[i]
            if arrow_img_path:
                arrow_x = x + TILE_SIZE // 2 + ARROW_OFFSET[direction][0] - ARROW_SIZE // 2
                arrow_y = y + TILE_SIZE // 2 + ARROW_OFFSET[direction][1] - ARROW_SIZE // 2
                self.draw_image(arrow_img_path, arrow_x, arrow_y, ARROW_SIZE)

    def draw_board(self, board):
        for row_index, row in enumerate(board.board):
            for col_index, field in enumerate(row):
                x_position, y_position = col_index * TILE_SIZE, row_index * TILE_SIZE

                if 3 <= row_index <= 6 and 3 <= col_index <= 6:
                    continue

                if (row_index, col_index) in START_TILES:
                    pygame.draw.rect(self.screen, START_TILES[(row_index, col_index)],
                                     (x_position, y_position, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(self.screen, BLACK, (x_position, y_position, TILE_SIZE, TILE_SIZE),
                                     GRID_WIDTH)

                if field.image and (row_index, col_index) not in NO_GRID_TILES:
                    pygame.draw.rect(self.screen, BLACK, (x_position, y_position, TILE_SIZE, TILE_SIZE),
                                     GRID_WIDTH)
                    self.draw_image(field.image, x_position + TILE_SIZE // 5, y_position + TILE_SIZE // 5,
                                    int(TILE_SIZE * 0.6))

                if field.arrow_images:
                    self.draw_arrows(field, x_position, y_position)

        self.draw_image(MIDDLE_IMAGE, 3 * TILE_SIZE, 3 * TILE_SIZE, TILE_SIZE * 4)

    def highlight_possible_moves(self, possible_moves):
        for row, col in possible_moves:
            x, y = col * TILE_SIZE, row * TILE_SIZE
            pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, (x, y, TILE_SIZE, TILE_SIZE), 3)

    def show_flash_card(self, card_type, text, color):
        curr_theme = pygame_menu.Theme(background_color=color, title_background_color=BLACK,
                                       title_font=pygame_menu.font.FONT_COMIC_NEUE, title_font_color=WHITE,
                                       widget_font_color=BLACK)
        flash_menu = pygame_menu.Menu(title=f"{card_type}", width=FLASH_CARD_WIDTH, height=FLASH_CARD_HEIGHT,
                                      theme=curr_theme)

        flash_menu.add.label(text, font_size=FONT_SIZE - 10, max_char=-1, font_color=BLACK)
        flash_menu.add.button("OK", flash_menu.disable)
        flash_menu.mainloop(self.screen)

    def render_all_players_money(self, players):
        money_title = FONT.render("Player Balances:", True, (255, 255, 255))
        self.screen.blit(money_title, (INFO_PANEL_X + 10, SCREEN_HEIGHT - 300))

        y_offset = SCREEN_HEIGHT - 260
        for player in players:
            money_text = FONT.render(f"Player {player.id + 1}: {player.money} ", True, player.color)
            self.screen.blit(money_text, (INFO_PANEL_X + 10, y_offset))
            y_offset += 40

    def render_ui(self, players, curr_player, dice):
        pygame.draw.rect(self.screen, (50, 50, 50), (INFO_PANEL_X, 0, INFO_PANEL_WIDTH, BOARD_WIDTH))

        player_text = FONT.render(f"Player {curr_player.id + 1}", True, PLAYER_COLORS[curr_player.id])
        self.screen.blit(player_text, (INFO_PANEL_X + 50, 50))

        dice.draw(self.screen)

        instructions = FONT.render("Click to Roll", True, WHITE)
        self.screen.blit(instructions, (INFO_PANEL_X + 50, 250))
        self.render_all_players_money(players)

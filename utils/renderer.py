import pygame

from constants import (GRID_COLOR, GRID_WIDTH, MIDDLE_IMAGE, START_TILES, NO_GRID_TILES, ARROW_SIZE, ARROW_OFFSET,
                       INFO_PANEL_WIDTH, BOARD_WIDTH, INFO_PANEL_X, TEXT_COLOR, FONT_SIZE, PLAYER_COLORS, TILE_SIZE,
                       HIGHLIGHT_COLOR, SCREEN_HEIGHT, WHITE)

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
                    pygame.draw.rect(self.screen, GRID_COLOR, (x_position, y_position, TILE_SIZE, TILE_SIZE),
                                     GRID_WIDTH)

                if field.image and (row_index, col_index) not in NO_GRID_TILES:
                    pygame.draw.rect(self.screen, GRID_COLOR, (x_position, y_position, TILE_SIZE, TILE_SIZE),
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

    @staticmethod
    def format_text_for_card(text, font, max_width, max_height):
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            text_width, _ = font.size(test_line)

            if text_width < max_width - 40: 
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "

        lines.append(current_line.strip())  
        
        while len(lines) * (font.get_height() + 5) > max_height - 40 and font.get_height() > 10:
            font = pygame.font.Font(None, font.get_height() - 2)
            lines = []
            current_line = ""

            for word in words:
                test_line = current_line + word + " "
                text_width, _ = font.size(test_line)

                if text_width < max_width - 40:
                    current_line = test_line
                else:
                    lines.append(current_line.strip())
                    current_line = word + " "

            lines.append(current_line.strip())

        return lines, font

    def draw_card_background(self, color, x, y, width, height):
        pygame.draw.rect(self.screen, color, (x, y, width, height), border_radius=15)
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, width, height), 3, border_radius=15)

    def show_flash_card(self, text, color):
        font = pygame.font.Font(None, FONT_SIZE)
        card_width, card_height = 300, 200
        card_x, card_y = INFO_PANEL_X // 2 - card_width // 2, BOARD_WIDTH // 2 - card_height // 2

        self.draw_card_background(color, card_x, card_y, card_width, card_height)
        lines, font = self.format_text_for_card(text, font, card_width, card_height)
        y_offset = card_y + 40
        for line in lines:
            text_surface = font.render(line, True, WHITE)
            text_rect = text_surface.get_rect(center=(card_x + card_width // 2, y_offset))
            self.screen.blit(text_surface, text_rect)
            y_offset += font.get_height() + 5

        pygame.display.flip()
        pygame.time.delay(3000)

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

        instructions = FONT.render("Click to Roll", True, TEXT_COLOR)
        self.screen.blit(instructions, (INFO_PANEL_X + 50, 250))
        self.render_all_players_money(players)

    def show_player_message(self, player):

        if player.last_message:
            font = pygame.font.Font(None, FONT_SIZE - 10)
            message_surface = font.render(player.last_message, True, TEXT_COLOR)
            message_rect = message_surface.get_rect(center=(INFO_PANEL_X + INFO_PANEL_WIDTH // 2, SCREEN_HEIGHT - 100))
            self.screen.blit(message_surface, message_rect)

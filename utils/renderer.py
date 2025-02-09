import pygame

from constants import (GRID_COLOR, GRID_WIDTH, MIDDLE_IMAGE, SPECIAL_TILES, NO_GRID_TILES, ARROW_SIZE, ARROW_OFFSET,
                       INFO_PANEL_WIDTH, BOARD_WIDTH, INFO_PANEL_X, TEXT_COLOR, FONT_SIZE, PLAYER_COLORS, TILE_SIZE,
                       HIGHLIGHT_COLOR, DICE_IMAGES, DICE_SIZE)

pygame.font.init()
FONT = pygame.font.Font(None, FONT_SIZE)


IMAGE_CACHE = {}

def get_image(image_path, size):
    if (image_path, size) not in IMAGE_CACHE:
        img = pygame.image.load(image_path)
        IMAGE_CACHE[(image_path, size)] = pygame.transform.scale(img, (size, size))
    return IMAGE_CACHE[(image_path, size)]

def draw_image(screen, image_path, x, y, size):
    screen.blit(get_image(image_path, size), (x, y))

def draw_arrows(screen, field, x, y):
    for i in range(len(field.arrow_directions)):
        direction = field.arrow_directions[i]
        arrow_img_path = field.arrow_images[i]
        if arrow_img_path:
            arrow_x = x + TILE_SIZE // 2 + ARROW_OFFSET[direction][0] - ARROW_SIZE // 2
            arrow_y = y + TILE_SIZE // 2 + ARROW_OFFSET[direction][1] - ARROW_SIZE // 2
            draw_image(screen, arrow_img_path, arrow_x, arrow_y, ARROW_SIZE)


def draw_board(screen, board):
    for row_index, row in enumerate(board.board):
        for col_index, field in enumerate(row):
            x_position, y_position = col_index * TILE_SIZE, row_index * TILE_SIZE

            if 3 <= row_index <= 6 and 3 <= col_index <= 6:
                continue

            if (row_index, col_index) in SPECIAL_TILES:
                pygame.draw.rect(screen, SPECIAL_TILES[(row_index, col_index)],
                                 (x_position, y_position, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, GRID_COLOR, (x_position, y_position, TILE_SIZE, TILE_SIZE), GRID_WIDTH)

            if field.image and (row_index, col_index) not in NO_GRID_TILES:
                pygame.draw.rect(screen, GRID_COLOR, (x_position, y_position, TILE_SIZE, TILE_SIZE), GRID_WIDTH)
                draw_image(screen, field.image, x_position + TILE_SIZE // 5, y_position + TILE_SIZE // 5,
                           int(TILE_SIZE * 0.6))

            if field.arrow_images:
                draw_arrows(screen, field, x_position, y_position)

    draw_image(screen, MIDDLE_IMAGE, 3 * TILE_SIZE, 3 * TILE_SIZE, TILE_SIZE * 4)


def highlight_possible_moves(screen, possible_moves):
    for row, col in possible_moves:
        x, y = col * TILE_SIZE, row * TILE_SIZE
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, (x, y, TILE_SIZE, TILE_SIZE), 3)


def render_ui(screen, current_player, dice):
    pygame.draw.rect(screen, (50, 50, 50), (INFO_PANEL_X, 0, INFO_PANEL_WIDTH, BOARD_WIDTH))

    player_text = FONT.render(f"Player {current_player + 1}", True, PLAYER_COLORS[current_player])
    screen.blit(player_text, (INFO_PANEL_X + 50, 50))

    dice.draw(screen)

    instructions = FONT.render("Click to Roll", True, TEXT_COLOR)
    screen.blit(instructions, (INFO_PANEL_X + 50, 250))

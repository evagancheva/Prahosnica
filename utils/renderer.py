import pygame

from constants import GRID_COLOR, GRID_WIDTH, MIDDLE_IMAGE, SPECIAL_TILES, NO_GRID_TILES,ARROW_SIZE, ARROW_OFFSET,TILE_SIZE



def draw_image(screen, image_path, x, y, size):
    img = pygame.image.load(image_path)
    img = pygame.transform.scale(img, (size, size))
    screen.blit(img, (x, y))


def draw_arrows(screen, field, x, y, tile_size):
    for direction, arrow_img_path in zip(field.arrow_directions, field.arrow_images):
        if arrow_img_path:
            arrow_x = x + TILE_SIZE // 2 + ARROW_OFFSET[direction][0] - ARROW_SIZE // 2
            arrow_y = y + TILE_SIZE // 2 + ARROW_OFFSET[direction][1] - ARROW_SIZE // 2
            draw_image(screen, arrow_img_path, arrow_x, arrow_y, ARROW_SIZE)

def render_board(screen, board, tile_size):
    for row_index, row in enumerate(board.board):
        for col_index, field in enumerate(row):
            x_position, y_position = col_index * tile_size, row_index * tile_size

            if 3 <= row_index <= 6 and 3 <= col_index <= 6:
                continue

            if (row_index, col_index) in SPECIAL_TILES:
                pygame.draw.rect(screen, SPECIAL_TILES[(row_index, col_index)],
                                 (x_position, y_position, tile_size, tile_size))
                pygame.draw.rect(screen, GRID_COLOR, (x_position, y_position, tile_size, tile_size), GRID_WIDTH)

            if field.image and (row_index, col_index) not in NO_GRID_TILES:
                pygame.draw.rect(screen, GRID_COLOR, (x_position, y_position, tile_size, tile_size), GRID_WIDTH)
                draw_image(screen, field.image, x_position + tile_size // 5, y_position + tile_size // 5,
                           int(tile_size * 0.6))

            if field.arrow_images:
                draw_arrows(screen, field, x_position, y_position, tile_size)

    draw_image(screen, MIDDLE_IMAGE, 3 * tile_size, 3 * tile_size, tile_size * 4)

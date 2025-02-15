import pygame

from constants import TILE_SIZE, PLAYER_COLORS, PLAYER_RADIUS


class Player:
    def __init__(self, start_row, start_col, player_id):
        self.row = start_row
        self.col = start_col
        self.color = PLAYER_COLORS[player_id]
        self.id = player_id
        self.possible_moves = []
        self.money = 1000

    def find_possible_moves(self, board, dice_result):
        if dice_result is None:
            return

        self.possible_moves = []

        def dfs(row, col, moves_left, path):
            if moves_left == 0:
                if (row, col) != (self.row, self.col):
                    self.possible_moves.append((row, col, path.copy()))
                return

            for direction in board.board[row][col].arrow_directions:
                new_row, new_col = row, col
                if direction == "left":
                    new_col -= 1
                elif direction == "right":
                    new_col += 1
                elif direction == "up":
                    new_row -= 1
                elif direction == "down":
                    new_row += 1

                if 0 <= new_row < len(board.board) and 0 <= new_col < len(board.board[0]):
                    path.append((new_row, new_col))
                    dfs(new_row, new_col, moves_left - 1, path)
                    path.pop()

        dfs(self.row, self.col, dice_result, [(self.row, self.col)])

    def animate_path(self, screen, renderer, path):
        for new_row, new_col in path:
            self.animate_movement(screen, renderer, new_row, new_col)

    def animate_movement(self, screen, renderer, new_row, new_col):
        renderer.update()
        renderer.draw_game()
        self.row, self.col = new_row, new_col
        self.draw(screen)
        pygame.display.flip()
        pygame.time.delay(50)

    def move_to(self, row, col, screen, renderer):
        for move in self.possible_moves:
            if move[:2] == (row, col):
                path = move[2]
                self.animate_path(screen, renderer, path)
                self.row, self.col = row, col
                self.possible_moves = []
                break

    def draw(self, screen):

        x = self.col * TILE_SIZE + TILE_SIZE // 2
        y = self.row * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.circle(screen, self.color, (x, y), PLAYER_RADIUS)

    def spend_money(self, amount):
        self.money -= amount

    def earn_money(self, amount):
        self.money += amount

    def is_winner(self):
        return self.money <= 0

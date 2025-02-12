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

        def dfs(row, col, moves_left):
            if moves_left == 0:
                if (row, col) != (self.row, self.col):
                    self.possible_moves.append((row, col))
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
                    dfs(new_row, new_col, moves_left - 1)

        dfs(self.row, self.col, dice_result)

    def move_to(self, row, col):
        if (row, col) in self.possible_moves:
            self.row = row
            self.col = col
            self.possible_moves = []

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

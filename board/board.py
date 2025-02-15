from board.field import Field
from constants import FIELD_IMAGES, ARROW_IMAGES, BOARD_LAYOUT, ARROW_LAYOUT


class Board:
    def __init__(self):
        """Initialize board"""
        self._grid_size = len(BOARD_LAYOUT)
        self.board = self._create_board()

    def _create_board(self):
        """Function that create board from Fields"""
        board = []
        for i in range(self._grid_size):
            row = []
            for j in range(self._grid_size):
                field_type = BOARD_LAYOUT[i][j]
                image = FIELD_IMAGES.get(field_type, None)

                arrow_directions = ARROW_LAYOUT[i][j]
                arrow_image = [ARROW_IMAGES.get(direction, None) for direction in arrow_directions]

                row.append(Field(field_type, image, arrow_image, arrow_directions))
            board.append(row)
        return board

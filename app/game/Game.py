from app.domain.Board import Board
from app.game.Snake import Snake


class Game:
    def __init__(self, rows, columns, count_apples):
        self._board = Board(rows, columns, count_apples)
        self._snake = Snake()

    @property
    def board(self):
        return self._board

    def move_steps(self, steps, direction):
        return self._snake.move(self._board, steps, direction)

    def change_direction(self, prev_direction, direction):
        return self._snake.move_direction(self._board, prev_direction, direction)
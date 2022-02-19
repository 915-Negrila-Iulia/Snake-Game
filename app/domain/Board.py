from random import randint

from texttable import Texttable


class Board:
    def __init__(self, rows, columns, apple_count):
        self._rows = rows
        self._columns = columns
        self._apple_count = apple_count
        self._board = [['' for i in range(self._columns)] for j in range(self._rows)]
        self._snake = self.display_snake()
        self.display_apples2(self._apple_count)
        #self.display_apples()

    @property
    def board(self):
        return self._board

    def rows(self):
        return self._rows

    def column(self):
        return self._columns

    def get_row(self, index):
        return self._board[index]

    def get_column(self, index):
        column = []
        for row in range(self._rows):
            column.append(self._board[row][index])
        return column

    def move_symbol(self, row, column, symbol):
        self._board[row][column]=symbol

    def get_box(self, row, column):
        return self._board[row][column]

    def add_apple(self):
        self.display_apples2(1)

    def get_snake(self):
        return self._snake

    def update_snake(self, row,column):
        self._snake.insert(0, [row,column])

    def cut_tail(self):
        self._snake.remove(self._snake[-1])

    def get_up(self):
        if self._snake[0][0] == 0:
            return False
        if [self._snake[0][0]-1, self._snake[0][1]] in self._snake:
            return False
        return self._snake[0][0]-1, self._snake[0][1]

    def get_left(self):
        if self._snake[0][1] == 0:
            return False
        if [self._snake[0][0], self._snake[0][1]-1] in self._snake:
            return False
        return self._snake[0][0], self._snake[0][1]-1

    def get_down(self):
        if self._snake[0][0] == self._rows-1:
            return False
        if [self._snake[0][0]+1, self._snake[0][1]] in self._snake:
            return False
        return self._snake[0][0]+1, self._snake[0][1]

    def get_right(self):
        if self._snake[0][1] == self._columns-1:
            return False
        if [self._snake[0][0], self._snake[0][1]+1] in self._snake:
            return False
        return self._snake[0][0], self._snake[0][1]+1

    def display_snake(self):
        """
        display the initial snake on board
        and create a list having the coordinates of the boxes which represent the snake
        :return: list representing the snake
        """
        snake = []
        row = self._rows // 2
        column = self._columns // 2
        self._board[row - 1][column] = '*'
        self._board[row][column] = '+'
        self._board[row + 1][column] = '+'
        snake.append([row - 1,column])
        snake.append([row,column])
        snake.append([row + 1,column])
        return snake

    def display_apples2(self, count_apples):
        """
        Place the initial apples on the board
        :param count_apples: integer representing the number of the apples on the board
        :return: -
        """
        for i in range(count_apples):
            ok=False
            while not ok:
                row = randint(1,self._rows-2)
                column = randint(1,self._columns-2)
                if self._board[row][column]=='' and self._board[row+1][column]!='.' \
                        and self._board[row-1][column]!='.' \
                         and self._board[row][column-1]!='.' \
                        and self._board[row][column+1]!='.':
                    self._board[row][column]='.'
                    ok=True

    def display_apples(self):
        for i in range(self._apple_count):
            ok=False
            row = randint(0,self._rows-1)
            column = randint(0,self._columns-1)
            while not ok:
                if self._board[row][column] == '':
                    if row!=0 and self._board[row-1][column]=='' or row==0:
                        if row!=self._rows-1 and self._board[row+1][column]=='' or row==self._rows-1:
                            if column!=0 and self._board[row][column-1]=='' or column == 0:
                                if column!=self._columns-1 and self._board[row][column+1]=='' or column==self._columns-1:
                                    self._board[row][column]='.'
                                    ok=True

    def __str__(self):
        t = Texttable()
        for row in range(self._rows):
            data_row = []
            for index in self._board[row]:
                if index == '':
                    data_row.append(' ')
                else:
                    data_row.append(index)  # *, +, .
            t.add_row(data_row)
        return t.draw()

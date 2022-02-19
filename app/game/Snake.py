class Snake:
    def move(self, board, steps, direction):
        for i in range(steps):
            if self.move_direction(board,direction,direction) is False:
                return False

    def move_direction(self, board, prev_direction, direction):
        if prev_direction == 'up' and direction == 'down' or \
                prev_direction == 'down' and direction == 'up' or \
                prev_direction == 'left' and direction == 'right' or \
                prev_direction == 'right' and direction == 'left':
            raise Exception("Can't change direction by 180degrees")

        if direction == 'up':
            if board.get_up() is False:
                return False
            row,column = board.get_up()

            if board.get_box(row,column)!='.':
                board.move_symbol(board.get_snake()[-1][0], board.get_snake()[-1][1], '')
                board.cut_tail()
            else:
                board.add_apple()

            board.update_snake(row,column)
            board.move_symbol(row,column,'*')
            board.move_symbol(board.get_snake()[1][0], board.get_snake()[1][1],'+')


        if direction == 'down':
            if board.get_down() is False:
                return False
            row,column = board.get_down()

            if board.get_box(row,column)!='.':
                board.move_symbol(board.get_snake()[-1][0], board.get_snake()[-1][1], '')
                board.cut_tail()
            else:
                board.add_apple()

            board.update_snake(row,column)
            board.move_symbol(row,column,'*')
            board.move_symbol(board.get_snake()[1][0], board.get_snake()[1][1],'+')

        if direction == 'left':
            if board.get_left() is False:
                return False
            row,column = board.get_left()

            if board.get_box(row,column)!='.':
                board.move_symbol(board.get_snake()[-1][0], board.get_snake()[-1][1], '')
                board.cut_tail()
            else:
                board.add_apple()

            board.update_snake(row,column)
            board.move_symbol(row,column,'*')
            board.move_symbol(board.get_snake()[1][0], board.get_snake()[1][1],'+')

        if direction == 'right':
            if board.get_right() is False:
                return False
            row,column = board.get_right()

            if board.get_box(row,column)!='.':
                board.move_symbol(board.get_snake()[-1][0], board.get_snake()[-1][1], '')
                board.cut_tail()
            else:
                board.add_apple()

            board.update_snake(row,column)
            board.move_symbol(row,column,'*')
            board.move_symbol(board.get_snake()[1][0], board.get_snake()[1][1],'+')
from app.game.Game import Game
from app.ui.properties import SettingsProperties


class Console:
    def __init__(self, rows, columns, count_apples):
        self._prev_direction='up'
        self._game = Game(rows,columns,count_apples)

    def split_command(self, command):
        splited = command.split(' ',1)
        name = splited[0]
        steps = splited[1]
        return name, int(steps)

    def start(self):
        done = False
        while not done:
            try:
                print(self._game.board)
                command=input('give command: ')
                if command in ['up','down','right','left']:
                    if self._game.change_direction(self._prev_direction, command) is False:
                        print('Game over')
                        done = True
                    self._prev_direction = command
                elif command == 'move':
                    if self._game.move_steps(1, self._prev_direction) is False:
                        print('Game over')
                        done = True
                else:
                    name,steps = self.split_command(command)
                    if name == 'move':
                        if self._game.move_steps(steps, self._prev_direction) is False:
                            print('Game over')
                            done = True
            except Exception as exception:
                print(str(exception))


settings_properties = SettingsProperties()
dictionary = settings_properties.settings_data

console = Console(int(dictionary["dim"]), int(dictionary["dim"]), int(dictionary["count"]))
console.start()
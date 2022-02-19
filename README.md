# Snake
Implemented a console-based version of the beloved [game of Snake](https://www.google.com/search?q=play+snake).
1. At program start the game area is displayed.
   - game area is a `DIM x DIM` matrix of squares that contains the snake and a number of `apple_count` apples
   - snake starts with a head segment (`*`) and two body segments (`+`) and is placed in the middle of the board
   - apples, represented as dots (`.`), are placed randomly so that two apples cannot be adjacent on the row or column, and cannot overlap the snake's starting position
   - values of `DIM` (odd natural number) and `apple_count` (natural number) are read from a settings file
   
2. Play the game. The user can move the snake using the following commands:
   - `move [n]`. This moves the snake `n` squares, in the direction it is currently facing. `move` with no parameters moves the snake by `1` square
   - `up | right | down | left` changes the snake's direction accordingly. Trying to change the snake's direction by 180 degrees will result in an error message
   - when the snake eats an apple, its tail grows by `1 square`. A new apple is immediately added to the game area, following the rules at `Point 1`
   
3. Game Over.
   - game ends when the snake hits the edge of the game area, or one of its own segments

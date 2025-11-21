# 1. Setup main classes - Done
# 2. Render an empty board - Done
# 3. Create the snake and render to board
# 4. Player controls
# 5. Check if player dies
# 6. Add apples and eating

class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction



class Apple:
    pass

# Prints the height
class Game:
    def __init__(self, height, width): # Defines height and width variables.
        self.height = height
        self.width = width

    def board_matrix(self):
        return [[None for _ in range(self.width)] for _ in range(self.height)] # Returns _ for each defined self.height and self.width.

    def render(self):
        matrix = self.board_matrix()
        for row in matrix:
            print(''.join(['.' if cell is None else str(cell) for cell in row])) # Prints a '.' to each space as defined in the height and width.

game = Game(10, 20)
game.render()
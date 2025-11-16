# 1. Setup main classes - Done
# 2. Render an empty board
# 3. Create the snake and render to board
# 4. Player controls
# 5. Check if player dies
# 6. Add apples and eating

class Snake:
    pass


class Apple:
    pass

# Prints the height
class Game:
    def __init__(self):
        self.height = 10
        self.width = 20

    def render(self):
        print("Height", self.height) 
        print("Width", self.width)

game = Game(10, 20)
game.render()
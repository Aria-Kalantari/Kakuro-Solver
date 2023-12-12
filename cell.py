WHITE = 0
CLUE = -1
BLACK = -2

DOWN = "down"
RIGHT = "right"

####################################################################################

class Cell:
    def __init__(self, position, category):
        self.position = position
        self.category = category

####################################################################################

class Clue:
    def __init__(self, direction, length, goal):
        self.direction = direction
        self.length = length
        self.goal = goal
        self.position = None

class ClueCell(Cell):
    def __init__(self, position, downClue, rightClue): 
        super().__init__(position, category=CLUE)
        self.downClue = downClue
        if downClue is not None:
            self.downClue.position = self.position
        self.rightClue = rightClue
        if rightClue is not None:
            self.rightClue.position = self.position

####################################################################################

class BlackCell(Cell):
    def __init__(self, position):
        super().__init__(position, category=BLACK)

####################################################################################

class WhiteCell(Cell):
    def __init__(self, position, value=0):
        super().__init__(position, category=WHITE)
        self.value = value


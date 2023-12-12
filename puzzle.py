from cell import Cell
from cell import Clue
from cell import ClueCell
from cell import BlackCell
from cell import WhiteCell

####################################################################################

WHITE = 0
CLUE = -1
BLACK = -2

DOWN = "down"
UP = "up"

####################################################################################

class KakuroPuzzle:
    def __init__(self, height, width, cells):
        self.height = height
        self.width = width
        self.cells = cells
        self.clues = self.__setClues()
        self.puzzle = self.__setPuzzle()
        self.printPuzzle()

    def __setClues(self):
        clues = []
        for cell in self.cells:
            if cell.category is CLUE:
                if cell.downClue is not None:
                    clues.append(cell.downClue)
                elif cell.rightClue is not None:
                    clues.append(cell.rightClue)
        return clues
    
    def __setPuzzle(self):
        puzzle = [[WhiteCell((i, j)) for j in range(self.width)] for i in range(self.height)]
        for cell in self.cells:
            puzzle[cell.position[0]][cell.position[1]] = cell
        return puzzle
    
    def printPuzzle(self):
        for i in range(self.height):
            print('|', end = "")
            for j in range(self.width):
                if self.puzzle[i][j].category == BLACK:
                    print('   X   |', end = "")
                if self.puzzle[i][j].category == WHITE:
                    if len( str(self.puzzle[i][j].value) ) == 2:
                        print(' ' + str(self.puzzle[i][j].value) + '    |', end = "")
                    else:    
                        print('  ' + str(self.puzzle[i][j].value) + '    |', end = "")    
                if self.puzzle[i][j].category == CLUE:
                    if self.puzzle[i][j].downClue is not None:
                        if len( str(self.puzzle[i][j].downClue.goal) ) == 2:
                            print(' ' + str(self.puzzle[i][j].downClue.goal) + '\\', end = "" )
                        else:
                            print('  ' + str(self.puzzle[i][j].downClue.goal) + '\\', end = "") 
                    else:
                        print('  ' +'N' + '\\', end = "")
                    
                    if self.puzzle[i][j].rightClue is not None:
                        if len( str(self.puzzle[i][j].rightClue.goal) ) == 2:
                            print(str(self.puzzle[i][j].rightClue.goal) + ' |', end = "")
                        else:
                            print(str(self.puzzle[i][j].rightClue.goal) + '  |', end = "") 
                    else:
                        print('N  |', end = "") 
            print('\n')
        print('\n\n')
        
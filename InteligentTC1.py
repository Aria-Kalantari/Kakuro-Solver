WHITE = 0
CLUE = -1
BLACK = -2

DOWN = "down"
RIGHT = "right"

####################################################################################

import copy
import timeit

from cell import Cell
from cell import Clue
from cell import ClueCell
from cell import BlackCell
from cell import WhiteCell

from puzzle import KakuroPuzzle

from csp import KakuroCSP
from csp import IntelligentKakuroCSP

from agent import KakuroAgent
from agent import IntelligentKakuroAgent

####################################################################################

cells = []

#row1
cells.append(BlackCell((0, 0)))
cells.append(BlackCell((0, 1)))
cells.append(ClueCell((0, 2), Clue(DOWN, 4, 30), None))
cells.append(ClueCell((0, 3), Clue(DOWN, 2, 4), None))
cells.append(ClueCell((0, 4), Clue(DOWN, 3, 24), None))
cells.append(BlackCell((0, 5)))
cells.append(ClueCell((0, 6), Clue(DOWN, 2, 4), None))
cells.append(ClueCell((0, 7), Clue(DOWN, 2, 16), None))

#row2
cells.append(BlackCell((1, 0)))
cells.append(ClueCell((1, 1), Clue(DOWN, 2, 16), Clue(RIGHT, 3, 19)))
cells.append(ClueCell((1, 5), Clue(DOWN, 3, 9), Clue(RIGHT, 2, 10)))

#row3
cells.append(ClueCell((2, 0), None, Clue(RIGHT, 7, 39)))

#row4
cells.append(ClueCell((3, 0), None, Clue(RIGHT, 2, 15)))
cells.append(ClueCell((3, 3), Clue(DOWN, 3, 23), Clue(RIGHT, 2, 10)))
cells.append(ClueCell((3, 6), Clue(DOWN, 4, 10), None))
cells.append(BlackCell((3, 7)))

#row5
cells.append(BlackCell((4, 0)))
cells.append(ClueCell((4, 1), None, Clue(RIGHT, 2, 16)))
cells.append(ClueCell((4, 4), Clue(DOWN, 3, 6), Clue(RIGHT, 2, 4)))
cells.append(ClueCell((4, 7), Clue(DOWN, 2, 16), None))

#row6
cells.append(BlackCell((5, 0)))
cells.append(ClueCell((4, 1), Clue(DOWN, 2, 14), None))
cells.append(ClueCell((5, 2), Clue(DOWN, 2, 16), Clue(RIGHT, 2, 9)))
cells.append(ClueCell((5, 5), Clue(DOWN, 2, 4), Clue(RIGHT, 2, 12)))

#row7
cells.append(ClueCell((6, 0), None, Clue(RIGHT, 7, 35)))

#row8
cells.append(ClueCell((7, 0), None, Clue(RIGHT, 2, 16)))
cells.append(ClueCell((7, 3), None, Clue(RIGHT, 3, 7)))
cells.append(BlackCell((7, 7)))

puzzle = KakuroPuzzle(8, 8, cells)

intelligentAgent = IntelligentKakuroAgent(copy.deepcopy(puzzle))
intelligentStart = timeit.default_timer()
intelligentAgent.solve()
intelligentStop = timeit.default_timer()
intelligentTime = intelligentStop - intelligentStart

print("intelligent agent solved the puzzle in: \t", str(intelligentTime))
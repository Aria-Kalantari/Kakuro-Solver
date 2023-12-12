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
cells.append(BlackCell((0, 2)))
cells.append(BlackCell((0, 3)))
cells.append(ClueCell((0, 4), Clue(DOWN, 7, 40), None))
cells.append(ClueCell((0, 5), Clue(DOWN, 2, 3), None))
cells.append(BlackCell((0, 6)))
cells.append(BlackCell((0, 7)))

#row2
cells.append(BlackCell((1, 0)))
cells.append(BlackCell((1, 1)))
cells.append(BlackCell((1, 2)))
cells.append(ClueCell((1, 3), Clue(DOWN, 3, 8), Clue(RIGHT, 2, 6)))
cells.append(BlackCell((1, 6)))
cells.append(BlackCell((1, 7)))

#row3
cells.append(BlackCell((2, 0)))
cells.append(BlackCell((2, 1)))
cells.append(ClueCell((2, 2), None, Clue(RIGHT, 3, 7)))
cells.append(ClueCell((2, 6), Clue(DOWN, 2, 3), None))
cells.append(ClueCell((2, 7), Clue(DOWN, 2, 14), None))

#row4
cells.append(BlackCell((3, 0)))
cells.append(ClueCell((3, 1), Clue(DOWN, 2, 6), None))
cells.append(ClueCell((3, 2), Clue(DOWN, 2, 4), Clue(RIGHT, 2, 10)))
cells.append(ClueCell((3, 5), Clue(DOWN, 3, 24), Clue(RIGHT, 2, 9)))

#row5
cells.append(ClueCell((4, 0), None, Clue(RIGHT, 7, 28)))

#row6
cells.append(ClueCell((5, 0), None, Clue(RIGHT, 2, 3)))
cells.append(ClueCell((5, 3), Clue(DOWN, 2, 17), Clue(RIGHT, 2, 17)))
cells.append(BlackCell((5, 6)))
cells.append(BlackCell((5, 7)))

#row7
cells.append(BlackCell((6, 0)))
cells.append(BlackCell((6, 1)))
cells.append(ClueCell((6, 2), None, Clue(RIGHT, 3, 23)))
cells.append(BlackCell((6, 6)))
cells.append(BlackCell((6, 7)))

#row8
cells.append(BlackCell((7, 0)))
cells.append(BlackCell((7, 1)))
cells.append(ClueCell((7, 2), None, Clue(RIGHT, 2, 16)))
cells.append(BlackCell((7, 5)))
cells.append(BlackCell((7, 6)))
cells.append(BlackCell((7, 7)))

puzzle = KakuroPuzzle(8, 8, cells)

puzzle = KakuroPuzzle(8, 8, cells)

intelligentAgent = IntelligentKakuroAgent(copy.deepcopy(puzzle))
intelligentStart = timeit.default_timer()
intelligentAgent.solve()
intelligentStop = timeit.default_timer()
intelligentTime = intelligentStop - intelligentStart

print("intelligent agent solved the puzzle in: \t", str(intelligentTime))
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
cells.append(ClueCell((0, 1), Clue(DOWN, 2, 10), None))
cells.append(ClueCell((0, 2), Clue(DOWN, 3, 10), None))
cells.append(BlackCell((0, 3)))
cells.append(BlackCell((0, 4)))
cells.append(BlackCell((0, 5)))
cells.append(BlackCell((0, 6)))
cells.append(BlackCell((0, 7)))
cells.append(ClueCell((0, 8), Clue(DOWN, 3, 23), None))
cells.append(ClueCell((0, 9), Clue(DOWN, 2, 16), None))

#row2
cells.append(ClueCell((1, 0), None, Clue(RIGHT, 2, 4)))
cells.append(ClueCell((1, 3), Clue(DOWN, 2, 17), None))
cells.append(BlackCell((1, 4)))
cells.append(BlackCell((1, 5)))
cells.append(BlackCell((1, 6)))
cells.append(ClueCell((1, 7), Clue(DOWN, 3, 17), Clue(RIGHT, 2, 16)))

#row3
cells.append(ClueCell((2, 0), None, Clue(RIGHT, 3, 23)))
cells.append(ClueCell((2, 4), Clue(DOWN, 5, 20), None))
cells.append(BlackCell((2, 5)))
cells.append(ClueCell((2, 6), Clue(DOWN, 5, 30), Clue(RIGHT, 3, 24)))

#row4
cells.append(BlackCell((3, 0)))
cells.append(ClueCell((3, 1), None, Clue(RIGHT, 3, 13)))
cells.append(ClueCell((3, 5), Clue(DOWN, 3, 20), Clue(RIGHT, 3, 23)))
cells.append(BlackCell((3, 9)))

#row5
cells.append(BlackCell((4, 0)))
cells.append(BlackCell((4, 1)))
cells.append(BlackCell((4, 2)))
cells.append(ClueCell((4, 3), None, Clue(RIGHT, 4, 11)))
cells.append(BlackCell((4, 8)))
cells.append(BlackCell((4, 9)))

#row6
cells.append(BlackCell((5, 0)))
cells.append(BlackCell((5, 1)))
cells.append(BlackCell((5, 2)))
cells.append(ClueCell((5, 3), Clue(DOWN, 3, 6), Clue(RIGHT, 3, 23)))
cells.append(BlackCell((5, 7)))
cells.append(BlackCell((5, 8)))
cells.append(BlackCell((5, 9)))

#row7
cells.append(BlackCell((6, 0)))
cells.append(BlackCell((6, 1)))
cells.append(ClueCell((6, 2), Clue(DOWN, 3, 7), Clue(RIGHT, 4, 25)))
cells.append(ClueCell((6, 7), Clue(DOWN, 2, 3), None))
cells.append(ClueCell((6, 8), Clue(DOWN, 3, 9), None))
cells.append(BlackCell((6, 9)))

#row8
cells.append(BlackCell((7, 0)))
cells.append(ClueCell((7, 1), Clue(DOWN, 2, 4), Clue(RIGHT, 3, 8)))
cells.append(ClueCell((7, 5), None, Clue(RIGHT, 3, 7)))
cells.append(ClueCell((7, 9), Clue(DOWN, 2, 4), None))

#row9
cells.append(ClueCell((8, 0), None, Clue(RIGHT, 3, 6)))
cells.append(BlackCell((8, 4)))
cells.append(BlackCell((8, 5)))
cells.append(ClueCell((8, 6), None, Clue(RIGHT, 3, 6)))

#row10
cells.append(ClueCell((9, 0), None, Clue(RIGHT, 2, 3)))
cells.append(BlackCell((9, 3)))
cells.append(BlackCell((9, 4)))
cells.append(BlackCell((9, 5)))
cells.append(BlackCell((9, 6)))
cells.append(ClueCell((9, 7), None, Clue(RIGHT, 2, 4)))

puzzle = KakuroPuzzle(10, 10, cells)

intelligentAgent = IntelligentKakuroAgent(copy.deepcopy(puzzle))
intelligentStart = timeit.default_timer()
intelligentAgent.solve()
intelligentStop = timeit.default_timer()
intelligentTime = intelligentStop - intelligentStart

print("intelligent agent solved the puzzle in: \t", str(intelligentTime))
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
cells.append(ClueCell((0, 3), Clue(DOWN, 2, 3), None))
cells.append(ClueCell((0, 4), Clue(DOWN, 3, 23), None))
cells.append(ClueCell((0, 5), Clue(DOWN, 9, 45), None))
cells.append(ClueCell((0, 6), Clue(DOWN, 2, 6), None))
cells.append(BlackCell((0, 7)))
cells.append(BlackCell((0, 8)))
cells.append(BlackCell((0, 9)))

#row2
cells.append(BlackCell((1, 0)))
cells.append(BlackCell((1, 1)))
cells.append(ClueCell((1, 2), None, Clue(RIGHT, 4, 12)))
cells.append(ClueCell((1, 7), Clue(DOWN, 2, 4), None))
cells.append(BlackCell((1, 8)))
cells.append(BlackCell((1, 9)))

#row3
cells.append(BlackCell((2, 0)))
cells.append(ClueCell((2, 1), Clue(DOWN, 4, 20), None))
cells.append(ClueCell((2, 2), Clue(DOWN, 5, 32), Clue(RIGHT, 5, 21)))
cells.append(ClueCell((2, 8), Clue(DOWN, 5, 15), None))
cells.append(BlackCell((2, 9)))

#row4
cells.append(ClueCell((3, 0), None, Clue(RIGHT, 2, 3)))
cells.append(ClueCell((3, 3), Clue(DOWN, 2, 17), Clue(RIGHT, 2, 15)))
cells.append(ClueCell((3, 6), Clue(DOWN, 2, 5), Clue(RIGHT, 2, 4)))
cells.append(ClueCell((3, 9), Clue(DOWN, 4, 16), None))

#row5
cells.append(ClueCell((4, 0), None, Clue(RIGHT, 3, 24)))
cells.append(ClueCell((4, 4), Clue(DOWN, 2, 16), Clue(RIGHT, 2, 3)))
cells.append(ClueCell((4, 7), Clue(DOWN, 2, 4), Clue(RIGHT, 2, 7)))

#row6
cells.append(ClueCell((5, 0), None, Clue(RIGHT, 9, 45)))

#row7
cells.append(ClueCell((6, 0), None, Clue(RIGHT, 2, 17)))
cells.append(ClueCell((6, 3), Clue(DOWN, 2, 13), Clue(RIGHT, 2, 17)))
cells.append(ClueCell((6, 6), Clue(DOWN, 3, 24), Clue(RIGHT, 3, 6)))

#row8
cells.append(BlackCell((7, 0)))
cells.append(ClueCell((7, 1), None, Clue(RIGHT, 2, 16)))
cells.append(ClueCell((7, 4), Clue(DOWN, 2, 17), Clue(RIGHT, 2, 15)))
cells.append(ClueCell((7, 7), Clue(DOWN, 2, 13), Clue(RIGHT, 2, 6)))

#row9
cells.append(BlackCell((8, 0)))
cells.append(BlackCell((8, 1)))
cells.append(ClueCell((8, 2), None, Clue(RIGHT, 5, 32)))
cells.append(BlackCell((8, 8)))
cells.append(BlackCell((8, 9)))

#row10
cells.append(BlackCell((9, 0)))
cells.append(BlackCell((9, 1)))
cells.append(BlackCell((9, 2)))
cells.append(ClueCell((9, 3), None, Clue(RIGHT, 4, 30)))
cells.append(BlackCell((9, 8)))
cells.append(BlackCell((9, 9)))


puzzle = KakuroPuzzle(10, 10, cells)

unintelligentAgent = KakuroAgent(copy.deepcopy(puzzle))
unintelligentStart = timeit.default_timer()
unintelligentAgent.solve()
unintelligentStop = timeit.default_timer()
unintelligentTime = unintelligentStop - unintelligentStart

print("unintelligent agent solved the puzzle in: \t", str(unintelligentTime))
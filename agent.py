from cell import Cell
from cell import Clue
from cell import ClueCell
from cell import BlackCell
from cell import WhiteCell

from puzzle import KakuroPuzzle

from csp import KakuroCSP
from csp import IntelligentKakuroCSP

import copy

####################################################################################

WHITE = 0
CLUE = -1
BLACK = -2

DOWN = "down"
RIGHT = "right"

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

####################################################################################

class KakuroAgent:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.csp = KakuroCSP()
    
    def solve(self):
        solution = self.__backtrackingSearch(self.puzzle)
        if solution is not None:
            self.puzzle = solution
            self.puzzle.printPuzzle()
        else:
            print("This puzzle has no solution.")
    
    def __backtrackingSearch(self, assignment):
        return self.__recursiveBacktracking(copy.deepcopy(assignment))

    def __recursiveBacktracking(self, assignment):
        if self.csp._isComplete(assignment): return assignment
        unassignedVariable = self.csp._selectUnassignedVariable(assignment)
        if unassignedVariable is not None:
            domainValues = self.csp._orderDomainValues(unassignedVariable)
            for value in domainValues:
                if self.csp._isConsistent(copy.deepcopy(assignment), unassignedVariable, value):
                    self.csp._assignValue(assignment, unassignedVariable, value)
                    assignment.printPuzzle()
                    result = self.__recursiveBacktracking(copy.deepcopy(assignment))
                    if result is not None: 
                        return result
        return None

####################################################################################

class IntelligentKakuroAgent(KakuroAgent):
    def __init__(self, puzzle):
        super().__init__(puzzle)
        self.csp = IntelligentKakuroCSP()
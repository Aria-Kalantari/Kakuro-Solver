from cell import Cell
from cell import Clue
from cell import ClueCell
from cell import BlackCell
from cell import WhiteCell

from puzzle import KakuroPuzzle

from random import randint
from operator import itemgetter
import copy

####################################################################################

WHITE = 0
CLUE = -1
BLACK = -2

DOWN = "down"
RIGHT = "right"

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

####################################################################################

class KakuroCSP:
    def _isComplete(self, assignment):
        if not self.__isConsistent(assignment):
            return False
        for i in range(assignment.height):
            for j in range(assignment.width):
                if assignment.puzzle[i][j].category == WHITE and assignment.puzzle[i][j].value == 0:
                    return False
        return True

    def _selectUnassignedVariable(self, assignment):
        clue = self._selectUnassignedClue(assignment)
        if clue is None:
            return clue
        else:
            variable = self._getVariable(assignment, clue)
            return variable


    def _selectUnassignedClue(self, assignment):
        for clue in assignment.clues:
            if not self._isVariableAssigned(self._getVariable(assignment, clue)):
                return clue 

    
    def _orderDomainValues(self, variable):
        domainValues = []
        assignedCells = []
        unassignedCells = []
        domain = DIGITS.copy()
        for cell in variable[1:]:
            if cell.value == 0:
                unassignedCells.append(cell)
            else:
                if cell.value in domain:
                    domain.remove(cell.value)
                assignedCells.append(cell)
        sum = 0
        for cell in assignedCells:
            sum += cell.value
        netGoal = variable[0].goal - sum
        netCellCount = variable[0].length - len(assignedCells)
        unassignedPossibleValues = self._sumEqualN(netGoal, netCellCount, domain)
        for unassignedPossibleValue in unassignedPossibleValues:
            variableCopy = copy.deepcopy(variable)
            domainValue = []
            for cell in variableCopy[1:]:
                if cell.value == 0:
                    domainValue.append(unassignedPossibleValue.pop(0))
                else:
                    domainValue.append(cell.value)
            domainValues.append(domainValue)
        return domainValues

    def __isConsistent(self, assignment):
        for clue in assignment.clues:
            variable = self._getVariable(assignment, clue)
            if self._isVariableAssigned(variable):
                values = []
                sum = 0
                for cell in variable[1:]:
                    values.append(cell.value)
                    sum += cell.value
                goal = clue.goal
                if not self._isConsistentInConstraintOne(values): 
                    return False
                if not self._isConsistentInConstraintTwo(sum, goal): 
                    return False
        return True
    
    def _isConsistent(self, assignment, variable, value):
        self._assignValue(assignment, variable, value)
        return self.__isConsistent(assignment)

    def _assignValue(self, assignment, variable, value):
        clue = variable[0]
        if clue.direction == DOWN:
            for i in range(clue.length):
                assignment.puzzle[clue.position[0] + i + 1][clue.position[1]].value = value[i]
        if clue.direction == RIGHT:
            for i in range(clue.length):
                assignment.puzzle[clue.position[0]][clue.position[1] + i + 1].value = value[i]

    def _getVariable(self, assignment, clue):
        variable = []
        if clue is None: 
            return variable
        variable.append(clue)
        if clue.direction == DOWN:
            for i in range(clue.length):
                variable.append(assignment.puzzle[clue.position[0] + i + 1][clue.position[1]])
        elif clue.direction == RIGHT:
            for i in range(clue.length):
                variable.append(assignment.puzzle[clue.position[0]][clue.position[1] + i + 1])
        return variable
    
    def _sumEqualN(self, n, k, domain):
        if k == 1 and n in domain:
            return [[n]]
        combos = []
        for i in domain:
            domainCopy = copy.deepcopy(domain)
            domainCopy.remove(i)
            if n - i > 0:
                combos += [[i] + combo for combo in self._sumEqualN(n - i, k - 1, domainCopy)]
        for combo in combos:
            if any(combo.count(x) > 1 for x in combo):
                combos.remove(combo)
        return combos

    def _isVariableAssigned(self, variable):
        for cell in variable[1:]:
            if cell.value == 0: 
                return False
        return True
    
    def _isConsistentInConstraintOne(self, values):
        for value in values:
            if values.count(value) > 1: 
                return False
        return True
    
    def _isConsistentInConstraintTwo(self, sum, goal): return sum == goal

####################################################################################

class IntelligentKakuroCSP(KakuroCSP):
    def _selectUnassignedVariable(self, assignment):
        clue = self._selectUnassignedClue(assignment)
        if clue is None:
            return clue
        else:
            variable = super()._getVariable(assignment, clue)
            return variable

    def _selectUnassignedClue(self, assignment):
        clue = self._MCV(assignment)
        return clue
    
    def _MCV(self, assignment):
        partialAssigned = []
        unassigned = []
        for clue in assignment.clues:
            count = self._unassignedCellCount(assignment, clue)
            if count == clue.length:
                unassigned.append((clue, count))
            elif count != 0:
                partialAssigned.append((clue, count))
        unassigned.sort(key=itemgetter(1))
        partialAssigned.sort(key=itemgetter(1))
        return (partialAssigned + unassigned)[0][0]
    
    def _unassignedCellCount(self, assignment, clue):
        variable = super()._getVariable(assignment, clue)
        count = 0
        for cell in variable[1:]:
            if cell.value == 0:
                count += 1
        return count
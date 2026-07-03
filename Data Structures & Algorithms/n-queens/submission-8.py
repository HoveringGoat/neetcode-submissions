class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # list of lists containing n ints with column indicies of the queen positions
        # eg: [0,1,2,3] for all diagonals
        possibleSolutions = []
        # the list of queen positions. it can be up to length n.
        # less elements mean we have only partially solved the potential solution
        currentSolution = []
        # find all possible solutions
        def recursiveQueens(currentSolution: List[int]):
            if len(currentSolution) == n:
                possibleSolutions.append(currentSolution)
                return

            # attempt to solve for placing a queen in every column of this row
            for index in range(n):
                #is it legal to place a queen here?
                if index in currentSolution:
                    # we already used this column
                    continue

                invalid = False
                for oldQueenRow in range(len(currentSolution)):
                    # we need to check if the new potential queen conflicts with a prior placement
                    oldQueenIndex = currentSolution[oldQueenRow]
                    row = len(currentSolution)

                    rowOffset = abs(oldQueenRow - row)
                    columnOffset = abs(oldQueenIndex - index)

                    if rowOffset == columnOffset:
                        # this is a diagonal position of a previous queen.
                        # mark invalid and check another position
                        invalid = True
                        break

                if invalid:
                    continue

                # new queen position is valid.
                # try to recursively solve for it
                newSolution = currentSolution[:]
                newSolution.append(index)
                recursiveQueens(newSolution)
        
        # take in the list of solutions and convert to expected format
        def convertSolutions(solutions: List[List[int]]) -> List[List[str]]:
            stringSolutions: List[List[str]] = []
            base = ['.'] * n
            for i in solutions:
                newSolve = []
                for j in i:
                    newSegment = base[:]
                    newSegment[j] = 'Q'
                    newSolve.append("".join(newSegment))
                
                stringSolutions.append((newSolve))
            return stringSolutions

            
        recursiveQueens(currentSolution)
        stringSolutions = convertSolutions(possibleSolutions)
        return stringSolutions
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getRow(rowNum:int) -> List[str]:
            row = board[rowNum]
            return row

        def getCol(colNum:int) -> List[str]:
            col: List[str] = []
            for row in board:
                col.append(row[colNum])
            return col

        def getBox(boxNum:int) -> List[str]:
            boxCol = boxNum % 3
            boxRow = int(boxNum/3)

            box: List[str] = []
            # first row

            for rowNum in range(boxRow*3, boxRow*3+3):
                row = getRow(rowNum)
                snip = row[boxCol*3:boxCol*3+3]
                box.extend(snip)
            return box

        def isValid(group: List[str]) -> bool:
            numberSet = set()
            for i in group:
                if i in numberSet:
                    return False
                if i != ".":
                    numberSet.add(i)
            return True

        # Check Rows
        for i in range(9):
            row = getRow(i)
            if (not isValid(row)):
                return False

        # Check Columns
        for i in range(9):
            col = getCol(i)
            if (not isValid(col)):
                return False
        
        # Check Boxes
        for i in range(9):
            box = getBox(i)
            if (not isValid(box)):
                return False
            
        return True





        
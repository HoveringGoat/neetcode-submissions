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

        for i in range(9):
            row = getRow(i)
            print(f"row{i}: {row}")
            if (not isValid(row)):
                print(f"row{i}: invalid!")
                return False
        for i in range(9):
            col = getCol(i)
            print(f"col{i}: {col}")
            if (not isValid(col)):
                print(f"col{i}: invalid!")
                return False
        for i in range(9):
            box = getBox(i)
            print(f"box{i}: {box}")
            if (not isValid(box)):
                print(f"box{i}: invalid!")
                return False
            
        return True





        
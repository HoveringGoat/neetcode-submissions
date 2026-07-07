class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            # Gets the group that represents row N
            def getRow(rowNum:int) -> List[str]:
                return board[rowNum]

            # Gets the group that represents column N
            def getCol(colNum:int) -> List[str]:
                col = []
                for row in board:
                    col.append(row[colNum])
                return col

            # Gets the group that represents box N
            def getBox(boxNum:int) -> List[str]:
                boxCol = boxNum % 3
                boxRow = int(boxNum/3)

                box: List[str] = []
                for rowNum in range(boxRow*3, boxRow*3+3):
                    row = getRow(rowNum)
                    snip = row[boxCol*3:boxCol*3+3]
                    box.extend(snip)
                return box

            # Check if the group is valid. No repeating numbers
            def isValid(group: List[str]) -> bool:
                group_set = set()
                for i in group:
                    if i == ".":
                        continue
                    if i in group_set:
                        return False
                    group_set.add(i)
                return True

            # Check Rows
            for i in range(9):
                row = getRow(i)
                #print(f"row{i}: {row}")
                if (not isValid(row)):
                    #print(f"row{i} invalid")
                    return False

            # Check Columns
            for i in range(9):
                col = getCol(i)
                #print(f"col{i}: {col}")
                if (not isValid(col)):
                    #print(f"col{i} invalid")
                    return False
            
            # Check Boxes
            for i in range(9):
                box = getBox(i)
                #print(f"box{i}: {box}")
                if (not isValid(box)):
                    #print(f"box{i} invalid")
                    return False
                
            return True
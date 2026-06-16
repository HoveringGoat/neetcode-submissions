class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # read through the board and at every char matching the first char try to find the word
        # mark used letters if we dead end, back out back to the brute search

        rowNum = 0
        for row in board:
            colNum = 0
            for letter in row:
                if letter == word[0]:
                    #print(f"({rowNum},{colNum}) Found letter: {letter}")
                    if self.checkAround(board, word, [], rowNum, colNum):
                        return True
                colNum += 1
            rowNum += 1
        return False


    def checkAround(self, board: List[List[str]], word: str, used:List[List], row: int, col: int) -> bool:
        def positionValid(position: List[int], used: List[List]) -> bool:
            if position[0] < 0 or position[0] >= len(board):
                return False
            if position[1] < 0 or position[1] >= len(board[0]):
                return False

            # in bounds. ensure its not used.
            if position in used:
                return False
            return True
        
        pos = [row,col]
        newUsed = used.copy()
        newUsed.append(pos)
        newWord = word[1:]

        if len(newWord) == 0:
            return True

        for i in [-1,0,1]:
            for j in [-1,0,1]:
                # only check adjacent grids
                if i != 0 and j != 0:
                    continue
                
                newPos = [pos[0]+i, pos[1] + j]
                if not positionValid(newPos, newUsed):
                    continue

                #print(f"({newPos[0]},{newPos[1]}) Valid position. Letter: {board[newPos[0]][newPos[1]]}")
                # valid position. has correct char???

                if board[newPos[0]][newPos[1]] == newWord[0]:
                    #print("found next letter!")
                    if self.checkAround(board, newWord, newUsed, newPos[0], newPos[1]):
                        return True
        
        return False
                
                    


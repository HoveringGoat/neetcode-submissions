class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # read through the board and at every char matching the first char try to find the word
        # mark used letters if we dead end, back out back to the brute search

        used = set()
        adjMap = {}
        for row in range(len(board)):
            for col in range(len(board[0])):
                letter = board[row][col]
                if letter in word:
                    letters = self.getAdjLetters(board, word, (row, col))
                    if letter in adjMap:
                        adjMap[letter].update(letters)
                    else:
                        adjMap[letter] = set(letters)

        #print(f"adjmap: {adjMap}")

        for row in range(len(board)):
            for col in range(len(board[0])):
                letter = board[row][col]
                if letter in word:
                    if self.checkContainsAdjacentLetters(adjMap, letter):
                        continue

                used.add((row,col))

        #print(f"Used: {used}")
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) in used:
                    continue
                letter = board[row][col]
                if letter == word[0]:
                    #print(f"({row},{col}) Found letter: {letter}")
                    if self.checkAround(board, word, used, (row, col)):
                        return True
        return False

    def getAdjLetters(self, board: List[List[str]], word:str, pos: Tuple[int]) -> List(str):
        def positionValid(position: Tuple[int]) -> bool:
            if position[0] < 0 or position[0] >= len(board):
                return False
            if position[1] < 0 or position[1] >= len(board[0]):
                return False

            return True
        
        def getValidPositions(pos:Tuple) -> List[Tuple[int]]:
            positions = []
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    # only check adjacent grids
                    if i != 0 and j != 0:
                        continue
                    
                    newPos = [pos[0]+i, pos[1] + j]
                    if not positionValid(newPos):
                        continue
                    positions.append(newPos)
            return positions

        letters = []
        for newPos in getValidPositions(pos):
            letter = board[newPos[0]][newPos[1]]
            if letter in word:
                letters.append(letter)
        return letters

    def checkAround(self, board: List[List[str]], word: str, used:Set[Tuple], pos:Tuple[int]) -> bool:
        def positionValid(position: Tuple[int], used:Set[Tuple]) -> bool:
            if position[0] < 0 or position[0] >= len(board):
                return False
            if position[1] < 0 or position[1] >= len(board[0]):
                return False

            # in bounds. ensure its not used.
            if (position[0], position[1]) in used:
                return False
            return True
        
        def getValidPositions(used:Set[Tuple], pos:Tuple) -> List[Tuple[int]]:
            positions = []
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    # only check adjacent grids
                    if i != 0 and j != 0:
                        continue
                    
                    newPos = [pos[0]+i, pos[1] + j]
                    if not positionValid(newPos, used):
                        continue
                    positions.append(newPos)
            return positions
        
        newUsed = used.copy()
        newUsed.add((pos[0], pos[1]))
        newWord = word[1:]

        if len(newWord) == 0:
            return True

        for newPos in getValidPositions(newUsed, pos):
            if board[newPos[0]][newPos[1]] == newWord[0]:
                #print(f"({newPos[0]},{newPos[1]}) Valid position. Letter: {board[newPos[0]][newPos[1]]}")
                if self.checkAround(board, newWord, newUsed, newPos):
                    return True
        
        return False
                
    def checkContainsAdjacentLetters(self, adjMap:dict, letter:str) -> bool:
        if letter in adjMap and len(adjMap[letter]) > 0:
            return True
        return False
                    


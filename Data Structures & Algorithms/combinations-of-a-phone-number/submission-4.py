class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        map = {}
        map["2"] = ["a","b","c"]
        map["3"] = ["d","e","f"]
        map["4"] = ["g","h","i"]
        map["5"] = ["j","k","l"]
        map["6"] = ["m","n","o"]
        map["7"] = ["p","q","r","s"]
        map["8"] = ["t","u","v"]
        map["9"] = ["w","x","y","z"]

        # trivial case - empty string
        if len(digits) == 0:
            return []

        # init solutions to the chars in the first digit
        solutions: List[str] = map[digits[0]]

        for i in digits[1:]:
            # for each digit get the mapped chars 
            chars = map[i]
            
            # copy current solutions to a temp list
            oldSolutions = solutions[:]
            # reset the solutions array so we can re-write it
            # our solution length will multiply by len(chars) each time (3x-4x)
            solutions = []

            # for each char in the chars list we will append it to a current solution
            # then re-add it to the updated solutions list
            for char_to_add in chars:
                for solution in oldSolutions:
                    solutions.append(solution + char_to_add)

        return solutions
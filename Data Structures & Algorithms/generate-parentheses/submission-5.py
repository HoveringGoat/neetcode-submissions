class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        def recursion(p_string: str, left: int, right: int):
            if left == n and right == n:
                combinations.append(p_string)
                return
            if left < n:
                recursion(p_string +'(', left+1, right)
            # only do right paren if valid
            if left > right:
                recursion(p_string +')', left, right+1)

        recursion("", 0, 0)
        return combinations







    def oldSolution(self, n: int) -> List[str]:
        combinations = []
        length = 2**(2*n)
        #print(f"length: {length}")
        for i in range(length):
            c = ""
            count = 0
            for j in range(n*2):
                b = 2 ** j
                if b & i:
                    count += 1
                    c+="("
                else:
                    count -= 1
                    c+=")"
                    if count < 0:
                        #print(f"{i}: invalid set:   {c}")
                        break
            if count == 0:
                #print(f"{i}: valid set:   {c}")
                combinations.append(c)
            
        return combinations

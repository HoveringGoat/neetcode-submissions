class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        combinations = []
        length = 2**(2*n)
        print(f"length: {length}")
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
            else: 
                #print(f"invalid set: {c}")
                pass
            
        return combinations


        
        # "((()))"
        # "()(())" 1, 1
        # "()()()" 1, 2
        # "(()())" 2, 1
        # "(())()" 2, 2

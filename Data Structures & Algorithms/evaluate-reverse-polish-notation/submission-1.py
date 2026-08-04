class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            
            if i == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
                #print(f"{a}{i}{b} = {stack[-1]}")
                continue
                
            if i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
                #print(f"{a}{i}{b} = {stack[-1]}")
                continue
                
            if i == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
                #print(f"{a}{i}{b} = {stack[-1]}")
                continue
                
            if i == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
                #print(f"{a}{i}{b} = {stack[-1]}")
                continue
            
            # number
            stack.append(int(i))
        
        return stack.pop()

        
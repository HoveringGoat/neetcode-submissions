class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                if i == "(":
                    stack.append(")")
                    continue
                if i == "[":
                    stack.append("]")
                    continue
                if i == "{":
                    stack.append("}")
                    continue
                return False
        return len(stack) == 0
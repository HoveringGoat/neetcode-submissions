class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_closed = {"(":")", "{":"}","[":"]"}

        for i in s:
            # closing bracket pops off stack
            if len(stack) > 0 and i == stack[-1]:
                stack.pop()
                continue

            # opening bracket OR its invalid
            stackDepth = len(stack)
            for j in open_to_closed.keys():
                if i == j:
                    stack.append(open_to_closed[j])
                    break

            # if nothing was added then it was invalid
            if stackDepth == len(stack):
                return False
        return len(stack) == 0
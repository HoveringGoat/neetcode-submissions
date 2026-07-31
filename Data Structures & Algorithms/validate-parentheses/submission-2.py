class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_closed = {"(":")", "{":"}","[":"]"}

        for i in s:
            # closing bracket pops off stack
            if len(stack) > 0 and i == stack[-1]:
                stack.pop()
                continue

            # opening bracket - add closing to stack
            if i in open_to_closed.keys():
                stack.append(open_to_closed[i])
                continue

            # not a opening bracket - invalid
            return False
        return len(stack) == 0
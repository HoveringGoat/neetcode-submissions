class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for i in s:
            c = i.lower()
            # valid char
            v = ord(c)
            if v >= 48 and v <= 57:
                stripped += c
            elif v >= 97 and v <= 123:
                stripped += c
        return stripped == stripped[::-1]
        
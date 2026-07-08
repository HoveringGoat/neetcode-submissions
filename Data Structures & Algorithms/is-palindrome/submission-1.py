class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        stripped = ""
        for i in lower:
            # valid char
            v = ord(i)
            if v >= 48 and v <= 57:
                stripped += i
            elif v >= 97 and v <= 123:
                stripped += i
        return stripped == stripped[::-1]
        
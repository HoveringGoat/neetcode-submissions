class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s1 = list(s)
        s1.sort()
        s2 = list(t)
        s2.sort()

        return s1 == s2

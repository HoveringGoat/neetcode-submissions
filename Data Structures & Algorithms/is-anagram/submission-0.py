class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = self.getChars(s)
        s2 = self.getChars(t)

        return s1 == s2

    def getChars(self, s: str) -> Dict[str, int]:
        map = {}
        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        return map
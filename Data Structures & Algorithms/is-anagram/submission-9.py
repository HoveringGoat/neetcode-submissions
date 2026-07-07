class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # get counts of all letters
        def getMapping(word:str):
            map = {}
            for char in word:
                if char in map:
                    map[char] += 1
                else:
                    map[char] = 1
            return map


        s_map = getMapping(s)
        t_map = getMapping(t)

        return s_map == t_map
        
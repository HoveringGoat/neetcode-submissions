import random
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        if windowSize > len(s2):
            return False
        
        # init required dict and set
        required = Counter(s1)
        required_set = set(s1)

        # slide the window through the list checking if the required chars are all satified
        left = 0
        right = 0
        while right < len(s2):

            char = s2[right]
            if char in s1:
                # update dict and if satisfied pop the set else ensure its added
                required[char] -= 1
                if required[char] == 0:
                    required_set.remove(char)
                else:
                    required_set.add(char)

            right += 1
            # check if required is empty
            if len(required_set) == 0:
                return True

            if right - left < windowSize:
                continue

            # move left in
            char = s2[left]
            if char in s1:
                # update dict and if satisfied pop the set else ensure its added
                required[char] += 1
                if required[char] == 0:
                    required_set.remove(char)
                else:
                    required_set.add(char)

            left += 1 

        return False

import random
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        if windowSize > len(s2):
            return False
        
        # init required dict and set
        required = Counter(s1)
        required_set = set(s1)
        for right in range(windowSize-1):
            char = s2[right]
            if char in s1:
                required[char] -= 1
                if required[char] == 0:
                    required_set.remove(char)
                else:
                    required_set.add(char)
        # slide the window through the list checking if the required chars are all satified
        left = 0
        for right in range(windowSize-1, len(s2)):
            window = s2[left:right+1]

            char = s2[right]
            if char in s1:
                required[char] -= 1
                if required[char] == 0:
                    required_set.remove(char)
                else:
                    required_set.add(char)


            #print(f"window: {window}, required: {required}, set: {list(required_set)}")
            # check if required is empty
            if len(required_set) == 0:
                return True

            # move left in
            char = s2[left]
            if char in s1:
                required[char] += 1
                if required[char] == 0:
                    required_set.remove(char)
                else:
                    required_set.add(char)

            left += 1 

        return False

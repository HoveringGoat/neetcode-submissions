import random
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        short = s1
        long = s2
        if len(short) > len(long):
            #print("early exit")
            return False
        for i in range(1000):
            #print(f"{short}")
            if short in long:
                return True
            s = list(short)
            random.shuffle(s)
            short = ''.join(s)
        return False

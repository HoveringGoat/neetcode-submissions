class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort()
            a = stones.pop()
            b = stones.pop()
            c = a-b
            if c > 0:
                stones.append(c)
        if len(stones) == 0:
            return 0
        return stones[0]

        
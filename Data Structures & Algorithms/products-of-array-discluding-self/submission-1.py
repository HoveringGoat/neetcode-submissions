class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max: float = 1
        zeroCount = 0
        for i in nums:
            if i == 0:
                zeroCount += 1
                continue
            max *= i
        
        if zeroCount > 1:
            output = [0] * len(nums)
            return output

        output = []
        for i in nums:
            if i == 0:
                output.append(int(max))
                continue
            if zeroCount > 0:
                output.append(0)
                continue
            output.append(int(max/i))
        return output
        
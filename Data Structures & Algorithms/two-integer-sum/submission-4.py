class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # count the occurance of each letter for quick lookups
        def getCounts(word:str):
            map = {}
            for char in word:
                if char in map:
                    map[char] += 1
                else:
                    map[char] = 1
            return map

        # two values in nums will sum to target.
        # convert nums to mapped dict with counts
        nums_map = getCounts(nums)
        firstIndex = -1
        secondNumValue = 0
        for index, i in enumerate(nums):
            if firstIndex == -1:
                secondNumValue = target - i
                if secondNumValue == i and nums_map[i] == 1:
                    continue
                if secondNumValue in nums_map:
                    firstIndex = index
                continue
            
            # find second index
            if i == secondNumValue:
                return [firstIndex, index]

        return []
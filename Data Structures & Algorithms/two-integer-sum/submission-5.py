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
            # check if we are looking for the first or second value
            if firstIndex == -1:
                # find the expected second value if i is the first
                secondNumValue = target - i
                
                # check if the expected value exists in our mapping
                if secondNumValue in nums_map:
                    # ensure if the value is equal to the current value we dont have only 1
                    # i and j need to be unique entries. so if the value is the same we need two in nums
                    if secondNumValue == i and nums_map[i] == 1:
                        continue

                    # record the index of the first value
                    firstIndex = index
                continue
            
            # find second index
            # we know the value we just need to find its index
            # once we have it we can return
            if i == secondNumValue:
                return [firstIndex, index]

        # we should never hit this since there should always be a pair that sums to target
        return []
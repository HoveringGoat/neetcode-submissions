class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # records the expected second value and index of first value
        # map[j] = index_i
        map = {}
        for index, i in enumerate(nums):
            # if i is in the map we have previously calculated its pair!
            if i in map:
                return [map[i], index]

            # we haven't so lets write it down incase we find it later
            # get the expected value of the paired number
            j = target - i
            map[j] = index
        return []
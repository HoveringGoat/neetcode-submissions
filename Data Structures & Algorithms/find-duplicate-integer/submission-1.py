class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(1) space solution (and no list modification)
        for index, i in enumerate(nums[:-1]):
            for j in nums[index+1:]:
                if i == j:
                    return i
        return 0

        # set solution
        # nums_set = set()
        # for i in nums:
        #     if i in nums_set:
        #         return i
        #     nums_set.add(i)
        # return 0
        
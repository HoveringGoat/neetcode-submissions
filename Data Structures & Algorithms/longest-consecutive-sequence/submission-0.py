class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # trivial case
        if len(nums) == 0:
            return 0

        longest: int = 0
        current: int = 1

        # sort the values
        # init last
        nums.sort()
        last = nums[0]

        # look through all values recording length when a new sequence ends
        for i in nums[1:]:
            if last == i:
                continue
            if last + 1 == i:

                current += 1
            else:
                if current > longest:
                    longest = current
                current = 1
            last = i

        if current > longest:
            longest = current
        return longest
        
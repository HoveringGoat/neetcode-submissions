class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right)//2

            # in left range
            if nums[mid] > target:
                right = mid - 1
                continue
            # in right range
            if nums[mid] < target:
                left = mid+1
                continue
            return mid
        
        return -1
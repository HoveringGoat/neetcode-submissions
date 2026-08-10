class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find edge
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right)//2
            if nums[left] > nums[mid]:
                right = mid
                continue
            if nums[mid] > nums[right]:
                left = mid
                continue
            break
        return min(nums[left], nums[right])








        
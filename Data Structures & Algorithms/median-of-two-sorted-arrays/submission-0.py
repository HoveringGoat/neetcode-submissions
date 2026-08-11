class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        nums.extend(nums1)
        nums.extend(nums2)
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            middle = (length - 1)//2
            return nums[middle]

        middle = (length)//2
        median = (nums[middle] + nums[middle-1]) / 2.0
        return median


            
        
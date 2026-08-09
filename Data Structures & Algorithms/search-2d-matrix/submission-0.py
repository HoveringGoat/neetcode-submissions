class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binSearch(nums: List[int], target):
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

        for row in matrix:
            if binSearch(row, target) >= 0:
                return True
        return False
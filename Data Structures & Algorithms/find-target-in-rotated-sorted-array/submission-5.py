class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def isAscending(l: List[int]) -> bool:
            if l[0] <= l[-1]:
                print(f"range: {l} is ascending")
                return True
            print(f"range {l} is descending")
            return False
        
        def isTargetInsideRange(l: List[int], t: int) -> bool:
            if isAscending(l):
                return isTargetInsideAscRange(l, t)
            
            return isTargetInsideDescRange(l, t)
        
        def isTargetInsideAscRange(l: List[int], t: int) -> bool:
            return l[0] <= t and l[-1] >= t
        
        def isTargetInsideDescRange(l: List[int], t:int) -> bool:
            return l[0] <= t or l[-1] >= t
        
        left = 0
        right = len(nums) - 1

        # shrink search space to the range with the target umber
        while left + 1 < right:
            mid = (left+right)//2

            print(f"left = {nums[left:mid+1]}, right = {nums[mid:right+1]}")
            # we found it
            if nums[mid] == target:
                return mid
            
            # is it in the left range?
            if isTargetInsideRange(nums[left:mid+1], target):
                print("in left range")
                right = mid
                continue
            
            # if its not in the left range its in the right range
            print("in right range")
            left = mid

        # size 1 and 2 arrays skip the while loop checks
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
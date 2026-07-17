class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums: List[int] = []
        
        for right in range(k, len(nums)+1):
            left = right - k
            window = nums[left:right]
            maximums.append(max(window))

        return maximums
        
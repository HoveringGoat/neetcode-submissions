class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums: List[int] = []

        # list keeping a running sorted list of the previous window
        lastWindowSorted: List[int] = nums[:k-1]

        for right in range(k, len(nums)+1):
            left = right - k
            #print(f"window: {nums[left:right]}")
            # remove nums[left] from last window. add nums[right]
            if left > 0:
                lastWindowSorted.remove(nums[left-1])
            lastWindowSorted.append(nums[right-1])
            lastWindowSorted.sort()
            #print(f"sortedWindow: {lastWindowSorted}")
            maximums.append(lastWindowSorted[-1])

        return maximums
        
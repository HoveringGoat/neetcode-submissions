class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums: List[int] = []
        maxIndexes: List[int] = []

        for right in range(k-1, len(nums)):
            left = right - k + 1
            if len(maxIndexes) > 0:
                # right is new max
                if nums[right] > nums[maxIndexes[-1]]:
                    maxIndexes.append(right)
                    maximums.append(nums[right])
                    continue

                # old max is still in range
                if maxIndexes[-1] >= left:
                    maximums.append(nums[maxIndexes[-1]])
                    continue

            # dunno. calc new max
            window = nums[left:right+1]
            max_v = window[0]
            max_i = 0
            for i, v in enumerate(window[1:]):
                if v >= max_v:
                    max_v = v
                    max_i = i+left+1
            
            maxIndexes.append(max_i)
            maximums.append(max_v)

        return maximums
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        # move left and right pointers in as their sum > target
        while left < right:
            sum = numbers[right] + numbers[left]
            # move right if sum is too high
            if sum > target:
                right -= 1
                continue
            # move left if sum is too low
            if sum < target:
                left += 1
                continue

            # found target
            # remember the array is 1-indexed so add 1
            return [left+1, right+1]
        return []
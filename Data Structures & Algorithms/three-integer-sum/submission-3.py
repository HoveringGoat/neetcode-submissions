class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        i_solves = set()

        for i in range(len(nums)):
            target = nums[i]
            if target in i_solves:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                #print(f"{i}: {target}, {left}: {nums[left]}, {right}: {nums[right]}, sum: {sum+target}")

                if sum + target > 0:
                    right -= 1
                    continue
                if sum + target < 0:
                    left += 1
                    continue

                #print(f"found solve: {[target,nums[left],nums[right]]}")
                #print(nums)
                s = [target,nums[left],nums[right]]
                if s not in solutions:
                    solutions.append(s)
                i_solves.add(target)
                last_left = nums[left]
                left += 1
                right -= 1
                while last_left == nums[left] and left < right:
                    last_left = nums[left]
                    left += 1

            # if left >= right:
            #     #no solution found rest right
            #     right = lastRight

        return solutions
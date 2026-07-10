class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        i_solves = set()

        # two sum but we try and get target for each value of nums
        for i in range(len(nums)):
            target = nums[i]
            
            # if we already searched this target value we can skip
            if target in i_solves:
                continue
            i_solves.add(target)

            # reset left/right
            left = i+1
            right = len(nums) - 1
            
            # do two sum!
            while left < right:
                sum = nums[left] + nums[right]

                if sum + target > 0:
                    right -= 1
                    continue

                if sum + target < 0:
                    left += 1
                    continue

                # found solution make sure its unique
                s = [target,nums[left],nums[right]]
                if s not in solutions:
                    solutions.append(s)
                
                # move left and right in to search for other solutions
                last_left = nums[left]
                left += 1
                right -= 1

                # this isn't necessary.
                # we could let the normal while loop weed out duplicate solutions
                # but we might as well look while we're here
                while last_left == nums[left] and left < right:
                    last_left = nums[left]
                    left += 1

        return solutions
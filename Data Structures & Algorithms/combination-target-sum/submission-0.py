class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def getCombinationsRecursive(currentSet: List[int], candidates: List[int], target: int) -> bool:
            # we solved!
            # since we are being smart we know this is a unique solve!
            if target == 0:
                sum_sets.append(currentSet)
                return

            # remove values too large
            while(len(candidates) > 0 and candidates[-1] > target):
                candidates.pop()
            
            # is no solution here?
            if len(candidates) == 0:
                return

            i = candidates[-1]
            # try getting the set with the current largest value
            newSet = currentSet[:]
            newSet.append(i)
            # dupe set to avoid muddying current skip set
            getCombinationsRecursive(newSet, candidates[:], target - i)
            
            # try getting the set without the current largest value
            getCombinationsRecursive(currentSet, candidates[:-1], target)
            return

        # generate all subsets:
        sum_sets = []
        # sorting probably speeds up the solve?
        nums.sort()
        length = len(nums)
        getCombinationsRecursive([], nums, target)

        return sum_sets
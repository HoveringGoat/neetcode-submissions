class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def getCombinationsRecursive(skipped: set[int], currentSet: List[int], candidates: List[int], target: int) -> bool:
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

            i = candidates.pop()
            # if the number hasnt previously been skipped
            # try getting the set with the current largest value
            if i not in skipped:
                newSet = currentSet[:]
                newSet.append(i)
                # dupe set to avoid muddying current skip set
                newSkipped = set(skipped)
                getCombinationsRecursive(newSkipped, newSet, candidates[:], target - i)
                
                skipped.add(i)
            
            newSet = currentSet[:]
            # try getting the set without the current largest value
            getCombinationsRecursive(skipped, newSet, candidates[:], target)
            return

        # generate all subsets:
        sum_sets = []
        # sorting probably speeds up the solve?
        candidates.sort()
        length = len(candidates)
        getCombinationsRecursive(set(),[], candidates, target)

        return sum_sets
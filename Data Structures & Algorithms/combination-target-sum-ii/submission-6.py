class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def getCombinationsRecursive(skipped: set[int], currentSet: List[int], candidates: List[int], target: int) -> bool:
            if target == 0:
                if currentSet not in sum_sets:
                    sum_sets.append(currentSet)
                return

            while(len(candidates) > 0 and candidates[-1] > target):
                candidates.pop()

            if len(candidates) == 0:
                return

            i = candidates.pop()
            if i not in skipped:
                newSet = currentSet[:]
                newSet.append(i)
                newSkipped = set(skipped)
                # try getting the set with the current largest value
                getCombinationsRecursive(newSkipped, newSet, candidates[:], target - i)
            
            newSet = currentSet[:]
            newSkipped = set(skipped)
            newSkipped.add(i)
            # try getting the set without the current largest value
            getCombinationsRecursive(newSkipped, newSet, candidates[:], target)
            return

        # generate all subsets:
        sum_sets = []
        candidates.sort()
        length = len(candidates)
        getCombinationsRecursive([],[], candidates, target)

        return sum_sets
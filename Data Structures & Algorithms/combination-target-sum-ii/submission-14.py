class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def getCombinationsRecursive(skipped, currentSet: List[int], candidates: List[int], target: int) -> bool:
            if target == 0:
                sum_sets.append(currentSet)
                return     
            if target < 0:
                return       
            if len(candidates) == 0:
                return

            i = candidates.pop()
            if i not in skipped:
                newSet = currentSet[:]
                newSet.append(i)
                # dupe set to avoid muddying current skip set
                newSkipped = set(skipped)
                getCombinationsRecursive(newSkipped, newSet, candidates[:], target - i)
            
            skipped.add(i)
            getCombinationsRecursive(skipped, currentSet, candidates[:], target)
            return

        # generate all subsets:
        sum_sets = []
        length = len(candidates)
        # candidates = [x for x in candidates if x <= target]
        candidates.sort()
        getCombinationsRecursive(set(),[], candidates, target)

        return sum_sets
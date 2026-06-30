class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        length = 2**(len(nums))
        subsets = []
        subsets_set = set()
        for i in range(length):
            newSet = []

            for j in range(len(nums)):
                b = 2 ** j
                if b & i:
                    newSet.append(nums[j])
            newSet.sort()
            s = str(newSet)
            if s not in subsets_set:
                subsets_set.add(s)
                subsets.append(newSet)
            
        return subsets
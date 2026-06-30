class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        length = 2**(len(nums))
        subsets = []
        subsets_set = set()
        for i in range(length):
            #print(f"i:{i}")
            # bitwise representation of i shows the "bytes" in the current set
            newSet = []

            for j in range(len(nums)):
                b = 2 ** j
                #print(f"{b}: {nums[j]}")
                if b & i:
                    #print(f"binary {j}: {b} & {i}")
                    newSet.append(nums[j])
            newSet.sort()
            s = str(newSet)
            if s not in subsets_set:
                subsets_set.add(s)
                subsets.append(newSet)
            
        return subsets
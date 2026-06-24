class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        allSubsets = []
        subKeys = set()

        def getSubsets(nums: List[int]) -> List[List[int]]:
            subbies = []
            for i in nums:
                copy = nums[:]
                copy.remove(i)
                if str(copy) not in subKeys:
                    subbies.append(copy)
                    subKeys.add(str(copy))
                    subbies.extend(getSubsets(copy))

            return subbies
        

        subs = [nums]
        subs.extend(getSubsets(nums))


        return subs
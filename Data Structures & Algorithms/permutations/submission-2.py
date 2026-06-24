class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def calcPermutations(subset: List[int]) -> List[List[int]]:
            if len(subset) == 1:
                return [subset]

            permutations = []
            num = subset[0]
            dupSubset = subset[1:]
            oldPermutations: List[List[int]] = permutationMap.get(str(dupSubset))

            for index in range(len(subset)):
                for permutation in oldPermutations:
                    prefix = permutation[0:index]
                    postFix = permutation[index:len(permutation)]
                    prefix.append(num)
                    prefix.extend(postFix)
                    permutations.append(prefix)

            return list(permutations)

        # dict of the calculated subset permutations
        # key is the stringified version of the substring
        permutationMap = {}

        # lets loop through the nums array and get all the permutations of each subset
        for subsetSize in range(1, len(nums)+1):
            for subsetIndex in range(0, len(nums) - subsetSize + 1 ):
                subset = nums[subsetIndex: subsetIndex+subsetSize]
                permutations = calcPermutations(subset)
                permutationMap[str(subset)] = permutations
        return permutationMap[str(nums)]
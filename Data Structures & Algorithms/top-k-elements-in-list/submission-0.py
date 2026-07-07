class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get counts of elements in list
        def getMapping(nums:List[int]):
            map = {}
            for num in nums:
                if num in map:
                    map[num] += 1
                else:
                    map[num] = 1
            return map

        # get counts of each number in the array
        # counts["number"] = "num_of_occurences"
        counts = getMapping(nums)
        
        # "sorts" the dictionary
        sortedNums = dict(sorted(counts.items(), key=lambda item: item[1]))

        # reverses the list to give a descending order
        # this will be the "key" so the number not the frequency
        descending = list(sortedNums.keys())[::-1]

        # get k top values
        return descending[:k]
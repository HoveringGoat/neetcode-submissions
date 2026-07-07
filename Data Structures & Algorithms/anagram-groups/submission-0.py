class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # "sorts" a word
        def sortString(word:str):
            l = []
            for char in word:
                l.append(char)
            l.sort()
            return ''.join(l)

        # the grouping of anagrams - key is the string sorted
        anagram_groups = {}

        for i in strs:
            # for each word, sort the string to easily compare anagram
            anagram = sortString(i)

            # if we already have the anagram group in the mapping append it to the list
            # otherwise make a new entry
            if anagram in anagram_groups:
                anagram_groups[anagram].append(i)
            else:
                anagram_groups[anagram] = [i]

        # return the groups values as a list
        return list(anagram_groups.values())


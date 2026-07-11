class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charPositions = {}
        longest = 0

        # iterate through the string
        for right, char in enumerate(s):
            # if this string is in our dict of mapped chars (and valid)
            # move left up to previously seen char position
            if char in charPositions and left <= charPositions[char]:
                left = charPositions[char] + 1

            # update dict entry to include new position
            charPositions[char] = right

            # calc length of current substring - len(s[left:right+1])
            length = right - left + 1

            # record longest
            if length > longest:
                longest = length

        return longest
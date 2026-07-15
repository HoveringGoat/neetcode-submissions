class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def getChars(word: str) -> dict[str, int]:
            map = {}
            for i in word:
                if i in map:
                    map[i] += 1
                else:
                    map[i] = 1
            return map

        t_chars = getChars(t)
        t_set = set(t_chars.keys())
        s_chars: dict[str, int] = {}
        # init values to required amount
        for c in t_set:
            s_chars[c] = 0

        unsatisfied = set(t_chars.keys())
        minSubstring: str = ""
        left: int = 0
        right: int = 0

        while right < len(s):
            char = s[right]

            # new char is in the target string
            if char in t_set:
                s_chars[char] += 1
                if s_chars[char] == t_chars[char]:
                    unsatisfied.remove(char)
            
            if len(unsatisfied) == 0:
                # move left up as much as possible while still satifying the substring
                while (left < right):
                    l_char = s[left]
                    if l_char in t_set:
                        # this char affects our substring counts
                        if s_chars[l_char] <= t_chars[l_char]:
                            # we must keep this char. left at max
                            break

                        # remove char from substring and counts
                        s_chars[l_char] -= 1
                    left += 1

                # compare new substring size
                size = right - left + 1
                if len(minSubstring) == 0 or size < len(minSubstring):
                    minSubstring = s[left:right+1]
            right += 1
                    
        return minSubstring
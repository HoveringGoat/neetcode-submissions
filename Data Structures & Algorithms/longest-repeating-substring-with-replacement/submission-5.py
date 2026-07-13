class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = -2
        end = -1
        char = ''
        left = 0
        right = 0
        maxSize = 0
        currSize = 0

        while start <= end and end + 1 < len(s) - 1:
            # move substring up
            start = end + 1
            for end in range(start, len(s)):
                if end+1 < len(s) and s[end+1] == s[start]:
                    continue
                break

            # we have found the start and end of the next substring
            char = s[start]
            left = start
            right = end

            # only do move logic if k > 0
            if k == 0:
                size = right - left + 1
                maxSize = max(maxSize, size)
                continue
            
            # move k places left
            leftK = 0
            while leftK < k and left > 0:
                left -= 1
                if s[left] != char:
                    leftK += 1

            # record size at max left
            size = right - left + 1
            maxSize = max(maxSize, size)

            # shift right k place
            rightK = 0

            # loop while budget isnt exhausted and right is in bounds
            while rightK <= k and right < len(s)-1:
                # always move right - check after if its valid
                right += 1
                if s[right] == char:
                    continue

                # uses right k budget
                rightK += 1 
                
                # we're at budget
                if rightK + leftK > k:
                    # if k buget exhausted move left back to the right
                    while leftK > 0 and rightK + leftK > k:
                        left += 1
                        if s[left-1] != char:
                            leftK -= 1

                    # we're either at budget now
                    # or leftKis zero and rightK is over utilizated

                    if rightK > k:
                        # we've gone too far right.
                        # move back and break
                        right -= 1
                        break
                    size = right - left + 1
                    maxSize = max(maxSize, size)

            # check size after exiting loop
            size = right - left + 1
            maxSize = max(maxSize, size)

        return maxSize

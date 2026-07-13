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
                # found end
                break
            #print(f"start:{start}, end:{end} - s:{s[start:end+1]}")
            char = s[start]
            left = start
            right = end

            # only do move logic if positive k
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

            #print(f"max left: {left} s: {s[left:end+1]}")
            size = right - left + 1
            maxSize = max(maxSize, size)

            # shift right k place
            rightK = 0
            while rightK <= k and right <= len(s)-1:
                #print(f"current: {left}-{right}, s: {s[left:right+1]}, size:{size}, k:{leftK}-{rightK}")
                
                if rightK == k and leftK == 0 and right < len(s)-1:
                    #print("move extra right")
                    right += 1
                    if s[right] != char:
                        #print("inc k")
                        rightK += 1
                        break
                # at k limit or right is at end of string
                if rightK + leftK >= k or right == len(s)-1:
                    size = right - left + 1
                    maxSize = max(maxSize, size)
                    #print(f"max left and right: {left}-{right}, s: {s[left:right+1]}, size:{size}")
                    if right == len(s)-1:
                        right += 1
                else:
                    #print("move right")
                    # move right
                    right += 1
                    if s[right] != char:
                        #print("inc k")
                        rightK += 1
               
                    if rightK + leftK >= k or right == len(s)-1:
                        size = right - left + 1
                        maxSize = max(maxSize, size)
                        #print(f"max left and right: {left}-{right}, s: {s[left:right+1]}, size:{size}")
 
                # if k buget exhausted move left back to the right
                while leftK > 0 and rightK + leftK >= k:
                    left += 1
                    if s[left-1] != char:
                        leftK -= 1


            

        return maxSize

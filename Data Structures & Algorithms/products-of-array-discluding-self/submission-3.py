class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # get the product of all nums less any zeros and count the instances of zero
        productAll: float = 1
        zeroCount = 0
        output = []
        for i in nums:
            if i == 0:
                zeroCount += 1
                continue
            productAll *= i
        
        # if we have more than 1 zero the whole thing is 0's
        if zeroCount > 1:
            output = [0] * len(nums)
            return output

        # we either have all non-zero numbers or one zero
        for i in nums:
            # for normal numbers we divide productAll by then number to get the product of all other numbers
            if zeroCount == 0:
                output.append(int(productAll/i))
                continue
                    
            # in the case we have a zero dont divide by it
            # we avoid using zeros in the product calc so its already accounted for
            if i == 0:
                output.append(int(productAll))
                continue
            # zero out all other entries
            output.append(0)
        return output
        
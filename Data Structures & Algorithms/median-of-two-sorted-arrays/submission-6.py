class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def findMedian(nums: List[int]) -> float:
            length = len(nums)
            if length % 2 == 1:
                middle = (length - 1)//2
                return nums[middle]

            middle = (length)//2
            median = (nums[middle] + nums[middle-1]) / 2.0
            return median

        left1 = 0
        right1 = len(nums1) - 1

        left2 = 0
        right2 = len(nums2) - 1

        # continue while there are values in both arrays
        while left1 <= right1 and left2 <= right2:
            #print(f"looping - nums1: {nums1[left1:right1+1]}, nums2: {nums2[left2:right2+1]}")
            # calc mids
            mid1 = (left1+right1)//2
            mid1_value = nums1[mid1]
            if (right1-left1) % 2 == 1:
                mid1_value = (mid1_value + nums1[mid1+1]) / 2.0

            mid2 = (left2+right2)//2
            mid2_value = nums2[mid2]
            if (right2-left2) % 2 == 1:
                mid2_value = (mid2_value + nums2[mid2+1]) / 2.0
            
            # solved?
            if mid1_value == mid2_value:
                return mid1_value

            # mid1 is lower - trim first half of nums1 and second of nums2
            if mid1_value < mid2_value:
                #print("mid1 less")
                # check if we can move left up
                if mid1 == left1 or mid2 == right2:
                    # if both values are already mid then we cannot shrink more.
                    if right1 == left1 and left2 == right2:
                        break
                    left1 += 1

                    # which right to shrink
                    if nums1[right1] > nums2[right2]:
                        right1 -= 1
                    else:
                        right2 -= 1
                else:
                    # remove x elements from left/right
                    diff1 = mid1 - left1
                    diff2 = right2 - mid2
                    diff = min(diff1, diff2)
                    #print(f"remove {diff} values")
                    left1 += diff

                    # is this a safe operation?
                    right2 -= diff
            else:
                #print("mid2 less")
                # check if we can move left up
                if mid2 == left2 or mid1 == right1:
                    # if both values are already mid then we cannot shrink more.
                    if right1 == left1 and left2 == right2:
                        break
                    left2 += 1

                    # which right to shrink
                    if nums2[right2] > nums1[right1]:
                        right2 -= 1
                    else:
                        right1 -= 1
                else:
                    # remove x elements from left/right
                    diff1 = mid2 - left2
                    diff2 = right1 - mid1
                    diff = min(diff1, diff2)
                    #print(f"remove {diff} values")

                    left2 += diff
                    right1 -= diff

        # if left1 <= right1:
        #     print(f"nums1: {nums1[left1:right1+1]}")
        # if left2 <= right2:
        #     print(f"nums2: {nums2[left2:right2+1]}")
        
        if left2 > right2:
            return findMedian(nums1[left1:right1+1])
        if left1 > right1:
            return findMedian(nums2[left2:right2+1])
            
        mid1 = (left1+right1)//2
        mid2 = (left2+right2)//2
        return (nums1[mid1] + nums2[mid2])/2.0






            
        
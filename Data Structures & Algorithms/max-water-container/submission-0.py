class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max = 0

        while left < right:
            # calc the distance of the container
            d = right - left

            # calc the height of the container (the smalled of the two values)
            h = heights[left]
            if heights[right] < heights[left]:
                h = heights[right]
            
            # calc area and save if its a max
            area = d * h
            if area > max:
                max = area
            
            # move left in
            if heights[left] < heights[right]:
                lastHeight = heights[left]
                while(heights[left] <= lastHeight and left < right):
                    left += 1
                continue
            
            # move right in
            lastHeight = heights[right]
            while(heights[right] <= lastHeight and left < right):
                right -= 1
        
        return max



                
        
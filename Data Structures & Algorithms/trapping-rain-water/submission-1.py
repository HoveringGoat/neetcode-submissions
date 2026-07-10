class Solution:
    def trap(self, height: List[int]) -> int:

        # walk through array and keep track any time we pass a new highest peak
        # when we do calc the amount trap from previous peak to new peak
        # save the trapped water amount if its a new maximum

        # This gives us valid results from start -> highest peak.
        # we don't know the water amount from peak -> end

        # since we know the highest peak index, iterate backwards through the list up to that index
        # we should then have a complete 
        
        global lastPeakIndex
        # gets the max trapped water in the list
        # uses global var of lastPeakIndex to track the index of the last peak
        def findMostWater(heights: List[int]) -> List[int]:
            waters: List[int] = []
            currentWater: int = 0
            lastPeakIndex: int = 0
            lastPeakHeight: int  = 0

            for index, height in enumerate(heights):
                # current water depth
                waterDepth = lastPeakHeight - height

                # negative/zero depth means new peak
                if waterDepth <= 0:
                    # add amount of water trapped between peaks
                    waters.append(currentWater)

                    # reset water
                    currentWater = 0

                    # record last peak info
                    lastPeakHeight = height
                    self.lastPeakIndex = index
                    continue
                
                # keep track of the amount of water we are scrolling past
                currentWater += waterDepth
            return waters

        waters = findMostWater(height)
        postPeakHeights = height[self.lastPeakIndex:]
        waters.extend (findMostWater(postPeakHeights[::-1]))
        return sum(waters)
                    
                
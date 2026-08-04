class Area:
    height: int
    start: int
    def __init__(self, start: int, height: int):
        self.start = start
        self.height = height

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # largest area so far
        maxArea: int = 0

        # the largest areas using the previous column
        previousAreas = []

        for column, height in enumerate(heights):
            newAreas = []
            maxAreaHeight = 0

            for area in previousAreas:
                if area.height <= height: 
                    size = (column - area.start + 1) * area.height
                    maxArea = max(size, maxArea)
                    newAreas.append(area)
                    maxAreaHeight = area.height
                    continue
                break
            
            for newAreaHeight in range(maxAreaHeight, height+1):
                area = Area(column, newAreaHeight)
                size = (column - area.start + 1) * area.height
                maxArea = max(size, maxArea)
                newAreas.append(area)
            
            previousAreas = newAreas

        return maxArea

            

        
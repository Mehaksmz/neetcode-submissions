class Solution:
    def maxArea(self, heights: List[int]) -> int: 
            l, r = 0, len(heights) - 1
            width = 0
            currMax = 0
            while l < r:
                width = r - l
                maxArea = min(heights[l], heights[r]) * width
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
                if maxArea > currMax:
                    currMax = maxArea     

            return currMax
            


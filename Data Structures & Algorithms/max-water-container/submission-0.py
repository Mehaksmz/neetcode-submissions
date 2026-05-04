class Solution:
    def maxArea(self, heights: List[int]) -> int:
        width = 0
        currMax = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = j - i
                maxArea = min(heights[i], heights[j]) * width
                if maxArea > currMax:
                    currMax = maxArea
        return currMax

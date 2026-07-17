class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxWater = 0
        while (left < right):
            currWater = 0
            if heights[left] <= heights[right]:
                currWater = heights[left] * (right - left)
                left += 1
            else:
                currWater = heights[right] * (right - left)
                right -= 1
            maxWater = max(currWater, maxWater)
        return maxWater
            

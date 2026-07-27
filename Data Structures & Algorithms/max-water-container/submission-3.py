class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxWater = 0
        while left <= right:
            if heights[left] <= heights[right]:
                maxWater = max(maxWater, (heights[left] * (right - left)))
                left += 1
            else:
                maxWater = max(maxWater, (heights[right] * (right - left)))
                right -= 1
        return maxWater
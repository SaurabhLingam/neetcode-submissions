class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                idx, h = stack.pop()
                w = i - idx
                maxArea = max(maxArea, h * w)
                start = idx
            stack.append((start, height))
        while stack:
            idx, h = stack.pop()
            w = len(heights) - idx
            maxArea = max(maxArea, h * w)
        return maxArea

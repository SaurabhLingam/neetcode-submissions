class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                w = index - idx
                maxArea = max(maxArea, h * w)
                start = idx
            stack.append((start, height))
        while stack:
            idx, h = stack.pop()
            width = len(heights) - idx
            maxArea = max(maxArea, h*width)
        return maxArea

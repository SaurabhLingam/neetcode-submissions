class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                idx, h = stack.pop()
                w = index - idx
                maxArea = max(maxArea, w * h)
                start = idx
            stack.append((start, height))

        while stack:
            idx, h = stack.pop()
            w = len(heights) - idx
            maxArea = max(maxArea, w * h)
        return maxArea
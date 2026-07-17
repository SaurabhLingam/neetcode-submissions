class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]
        maxRight = [0]
        for i in range(1, len(height)):
            maxLeft.append(max(maxLeft[i-1], height[i-1]))
        for i in range(len(height)-2, -1, -1):
            maxRight.append(max(maxRight[-1], height[i+1]))

        maxRight.reverse()
        total = 0
        for i in range(len(height)):
            total += max(0, min(maxLeft[i], maxRight[i]) - height[i])

        return total
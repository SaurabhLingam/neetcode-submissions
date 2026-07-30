class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        res = 0
        for i in range(n-2):
            res = first + second
            first = second
            second = res
        return res if n > 2 else n
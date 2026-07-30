class Solution:
    res = {}
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        elif n in self.res:
            return self.res[n]
        else:
            self.res[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
            return self.res[n]
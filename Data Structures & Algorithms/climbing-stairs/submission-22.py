class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,2,3]
        res = 0
        for i in range(4, n+1):
            arr.append(arr[-1] + arr[-2])
        return arr[n-1]
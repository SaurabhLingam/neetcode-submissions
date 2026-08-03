class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        dp = [0] * ((s//2)+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(s//2, -1, -1):
                if dp[j] and j + nums[i] <= s//2:
                    dp[j+nums[i]] = True
        return dp[s//2] == 1
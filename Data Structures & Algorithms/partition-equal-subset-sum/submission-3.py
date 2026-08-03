class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums) % 2) != 0:
            return False
        dp = [0] * (sum(nums)//2 + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(sum(nums)//2, -1, -1):
                if dp[j] and j+nums[i] <= (sum(nums)//2):
                    dp[j + nums[i]] = True
        return dp[sum(nums)//2] == 1
        
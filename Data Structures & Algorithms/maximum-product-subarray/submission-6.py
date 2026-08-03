class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            currmax = nums[i] * maxProd
            currmin = nums[i] * minProd
            maxProd = max(nums[i], currmin, currmax)
            minProd = min(nums[i], currmin, currmax)
            res = max(res, maxProd)
        return res
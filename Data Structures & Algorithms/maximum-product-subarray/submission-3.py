class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            currmax = nums[i] * maxProd
            currmin = nums[i] * minProd
            maxProd = max(nums[i], currmax, currmin)
            minProd = min(nums[i], currmax, currmin)
            result = max(result, maxProd)
        return result
class Solution:
    def robber(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(nums[i] + first, second)
            first = second
            second = curr
        return max(first, second)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first = self.robber(nums[0:-1])
        second = self.robber(nums[1:])
        return max(first, second)

        

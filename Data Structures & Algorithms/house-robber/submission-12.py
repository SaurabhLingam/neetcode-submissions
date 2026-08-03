class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(nums[i] + first, second)
            first = second
            second = curr
        return max(first, second)
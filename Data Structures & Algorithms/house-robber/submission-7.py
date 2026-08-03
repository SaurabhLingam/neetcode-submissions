class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        first = nums[0]
        second = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            curr = max(nums[i] + first, second)
            first = second
            second = curr
        return max(first, second)

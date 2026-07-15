class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fp = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in fp:
                return [fp[comp], i]
            else:
                fp[num] = i

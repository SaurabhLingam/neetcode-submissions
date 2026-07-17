class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        res = []
        first_index = 0
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hp:
                return [hp[comp], i]
            else:
                hp[num] = i
        return res

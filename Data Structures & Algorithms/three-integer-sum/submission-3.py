class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortnums = sorted(nums)
        res = []
        for i in range(len(sortnums)):
            if i > 0 and sortnums[i] == sortnums[i-1]:
                continue
            left = i + 1    
            right = len(sortnums) - 1
            while left < right:
                if sortnums[left] + sortnums[right] > 0 - sortnums[i]:
                    right -= 1
                elif sortnums[left] + sortnums[right] < 0 - sortnums[i]:
                    left += 1
                else: 
                    res.append([sortnums[i], sortnums[left], sortnums[right]])
                    left += 1
                    while left < right and sortnums[left] == sortnums[left - 1]:
                        left += 1
                    right -= 1
        return res
                    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortnums = set(nums)
        count = 0
        for num in sortnums:
            if num - 1 not in sortnums:
                tempcount = 1
                while num + 1 in sortnums:
                    tempcount += 1
                    num += 1
                count = max(count, tempcount)
            
        return count
            
        
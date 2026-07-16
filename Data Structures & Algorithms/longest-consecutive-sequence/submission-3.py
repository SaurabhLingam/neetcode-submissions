class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortnum = set(nums)
        count = 0
        for num in sortnum:
            if num - 1 not in sortnum:
                temp_count = 1
                while num + 1 in sortnum:
                    temp_count += 1
                    num += 1
                count = max(count, temp_count)
        return count
            
        
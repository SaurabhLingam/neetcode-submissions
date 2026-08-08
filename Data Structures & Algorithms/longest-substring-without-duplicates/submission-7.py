class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        maxLen = 0
        for end, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = end
            currLen = end - start + 1
            if currLen > maxLen:
                maxLen = currLen
        return maxLen
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        count = 0
        hm = {}
        while right < len(s):
            if s[right] in hm and hm[s[right]] >= left:
                left = hm[s[right]] + 1
                hm[s[right]] = right
                count = max(count, right - left + 1)
                right += 1
            else:
                hm[s[right]] = right
                count = max(count, right - left + 1)
                right += 1

        return count

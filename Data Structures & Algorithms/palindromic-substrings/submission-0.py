class Solution:
    def helper(self, left, right, s: str):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            odd = self.helper(i, i, s)
            even = self.helper(i, i+1, s)
            count += odd + even
        return count
        
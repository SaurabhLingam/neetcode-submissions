class Solution:
    def helper(self, left, right, s: str):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]
    def longestPalindrome(self, s: str) -> str:
        curr = ""
        for i in range(len(s)):
            odd = self.helper(i, i, s)
            even = self.helper(i, i+1, s)
            if len(curr) < len(odd):
                curr = odd
            if len(curr) < len(even):
                curr = even

        return curr
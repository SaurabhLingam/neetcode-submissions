class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        right = 0
        max_freq = 0
        count = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])
            if (right - left + 1) - max_freq <= k:
                count = max(count, right - left + 1)
                right += 1
            else:
                freq[s[left]] -= 1
                left += 1
                right += 1
        return count
                
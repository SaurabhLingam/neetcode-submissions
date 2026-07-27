class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        right = 0
        count = 0
        maxFreq = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])
            if (right - left + 1) - maxFreq <= k:
                count += 1
                right += 1
            else:
                freq[s[left]] -= 1
                left += 1
                right += 1
        return count
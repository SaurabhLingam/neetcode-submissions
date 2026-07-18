class Solution:
    def minWindow(self, s: str, t: str) -> str:
        right = 0
        left = 0
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1
        
        need = len(freq)
        min_len = float("inf")
        min_left = 0
        while right < len(s):
            if s[right] in freq:
                freq[s[right]] -= 1
                if freq[s[right]] == 0:
                    need -= 1
            while need == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                if s[left] in freq:
                    if freq[s[left]] == 0:
                        need += 1
                    freq[s[left]] += 1
                left += 1
            right += 1
        return str(s[min_left : min_left + min_len]) if min_len != float("inf") else ""
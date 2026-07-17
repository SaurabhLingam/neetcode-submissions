class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1
        res_left, res_len = 0, float('inf')
        need = len(freq)
        while right < len(s):
            if s[right] in freq:
                freq[s[right]] -= 1
                if freq[s[right]] == 0:
                    need -= 1
            while need == 0:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res_left = left
                if s[left] in freq:
                    if freq[s[left]] == 0:
                        need += 1
                    freq[s[left]] += 1
                left += 1
            right += 1
        return str(s[res_left : res_left + res_len]) if res_len != float('inf') else ""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1
        need = len(freq)
        minlen = float("inf")
        minleft = 0
        while right < len(s):
            if s[right] in freq:
                freq[s[right]] -= 1
                if freq[s[right]] == 0:
                    need -= 1
            
            while need == 0:
                if right - left + 1 < minlen:
                    minlen = right - left + 1
                    minleft = left
                if s[left] in freq:
                    if freq[s[left]] == 0:
                        need += 1
                    freq[s[left]] += 1
                left += 1
            right += 1
        return s[minleft : minleft + minlen] if minlen != float("inf") else ""

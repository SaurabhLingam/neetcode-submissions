class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        freq = {}
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        need = len(freq)
        print(need)
        while right < len(s2):
            if s2[right] in freq:
                freq[s2[right]] -= 1
                if freq[s2[right]] == 0:
                    need -= 1
            if right - left + 1 > len(s1):
                if s2[left] in freq:
                    if freq[s2[left]] == 0:
                        need += 1
                    freq[s2[left]] += 1
                left += 1
            right += 1

            if need == 0:
                return True
        return False

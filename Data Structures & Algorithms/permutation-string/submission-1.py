class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = defaultdict(int)
        perm2 = defaultdict(int)

        for c in s1:
            perm[c] += 1

        l = 0

        for r in range(len(s2)):
            perm2[s2[r]] += 1
            if perm == perm2:
                return True

            while perm2[s2[r]] > perm[s2[r]]:
                perm2[s2[l]] -= 1
                l += 1

        return False
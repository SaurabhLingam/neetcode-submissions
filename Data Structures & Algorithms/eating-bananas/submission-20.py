class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2
            th = 0
            for p in piles:
                th += (p + mid - 1)// mid
            if th > h:
                low = mid + 1
            else:
                high = mid - 1
        return low

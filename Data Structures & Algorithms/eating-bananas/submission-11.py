class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2
            total_time = 0
            for pile in piles:
                total_time += (pile + mid - 1) // mid
            if total_time > h:
                low = mid + 1
            else:
                high = mid - 1
        return low
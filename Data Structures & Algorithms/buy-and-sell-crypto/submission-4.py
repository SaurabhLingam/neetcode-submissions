class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo = float("inf")
        profit = 0
        for hi in prices:
            if hi < lo:
                lo = hi
            if hi - lo > profit:
                profit = hi - lo
        return profit
            


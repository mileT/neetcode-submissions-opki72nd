class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp1Allow, dp1NotAllow, dp2Allow = 0, 0, 0

        for i in range(n - 1, -1, -1):
            dpAllow = max(dp1Allow, dp1NotAllow - prices[i])
            dpNotAllow = max(dp1NotAllow, dp2Allow + prices[i])
            dp2Allow = dp1Allow
            dp1Allow, dp1NotAllow = dpAllow, dpNotAllow

        return dp1Allow
        
class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        n = len(prices)

        def dfs(i: int, canBuy: bool, memo: dict) -> int:
            if i >= n:
                return 0

            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            if canBuy:
                buy = dfs(i + 1, False, memo) - prices[i]
                skip = dfs(i + 1, True, memo)
                memo[(i, canBuy)] = max(buy, skip)
            else:
                sell = dfs(i + 2, True, memo) + prices[i]
                hold = dfs(i + 1, False, memo)
                memo[(i, canBuy)] = max(sell, hold)

            return memo[(i, canBuy)]

        return dfs(0, True, {})

    def maxProfit_2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            # can buy at i
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1] - prices[i]) # skip or buy at i
            # NOT allowed buy at i
            dp[i][1] = max(dp[i + 1][1], dp[i + 2][0] + prices[i]) # hold or sell at i

        return dp[0][0]
        
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        dp1Buy, dp1Sell, dp2Buy = 0, 0, 0

        for i in range(n - 1, -1, -1):
            dpBuy = max(dp1Buy, dp1Sell - prices[i])
            dpSell = max(dp1Sell, dp2Buy + prices[i])
            dp2Buy = dp1Buy
            dp1Buy, dp1Sell = dpBuy, dpSell

        return dp1Buy

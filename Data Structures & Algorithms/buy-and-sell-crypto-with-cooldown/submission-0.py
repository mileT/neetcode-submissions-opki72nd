class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
        
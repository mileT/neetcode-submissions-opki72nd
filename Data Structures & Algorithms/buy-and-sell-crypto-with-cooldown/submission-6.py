class Solution:
    def maxProfitDFS(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {} # key = (i, canBuy), val = profit

        def dfs(i, canBuy) -> int:
            if i >= n:
                return 0
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            skip = dfs(i + 1, canBuy)
            if canBuy:
                buy = dfs(i + 1, False) - prices[i]
                memo[(i, canBuy)] = max(buy, skip)
            else:
                sell = dfs(i + 2, False) + prices[i]
                memo[(i, canBuy)] = max(sell, skip)

            return memo[(i, canBuy)]

        return dfs(0, True)

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for canBuy in [True, False]:
                if canBuy:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    skip = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][True] = max(buy, skip)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    skip = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][False] = max(sell, skip)

        return dp[0][1]


        
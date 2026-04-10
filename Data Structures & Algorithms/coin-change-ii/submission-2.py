class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        coins.sort()
        dp = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(amount, coins, i):
            if i == len(coins):
                return 0
            if amount == 0:
                return 1
            
            if dp[i][amount] != -1:
                return dp[i][amount]

            result = 0
            if amount >= coins[i]:
                result = dfs(amount, coins, i + 1) + dfs(amount - coins[i], coins, i)
            dp[i][amount] = result

            return dp[i][amount] 

        return dfs(amount, coins, 0)

            
        
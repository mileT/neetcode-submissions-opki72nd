class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        coins.sort()
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]
        
        return dp[0][amount]

            
        
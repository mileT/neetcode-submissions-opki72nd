class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = 0
        n = len(coins)
        dict = {}

        def dfs(remain):
            if remain < 0:
                return -1
            if remain == 0:
                return 0;
            if remain in dict:
                return dict[remain]

            result = 1e9
            for coin in coins:
                if remain - coin >= 0:
                    result = min(result, 1 + dfs(remain - coin))
            
            dict[remain] = result
            return result

        minNum = dfs(amount)
        return -1 if minNum >= 1e9 else minNum

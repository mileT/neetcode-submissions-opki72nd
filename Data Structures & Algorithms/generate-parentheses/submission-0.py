class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(0, 0, n, [''] * n * 2, result)
        return result

    def dfs(self, l: int, r: int, n: int, cur: List[str], result: List[str]):
        if l + r == n * 2:
            result.append("".join(cur))
            return
        if l < n:
            cur[l + r] = '('
            self.dfs(l + 1, r, n, cur, result)
        if r < l:
            cur[l + r] = ')'
            self.dfs(l, r + 1, n, cur, result)
        
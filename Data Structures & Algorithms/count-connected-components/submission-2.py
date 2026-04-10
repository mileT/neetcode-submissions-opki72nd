class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(n)}
        visit = [False] * n
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            for nei in adj_list[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        result = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                result += 1

        return result
        
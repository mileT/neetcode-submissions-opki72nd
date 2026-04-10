class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(n)}
        visit = [False] * n

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nei in adj_list[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        result = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                result += 1

        return result
        
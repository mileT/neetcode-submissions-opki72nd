class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(n)}
        visited = set()
        result = 0

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(node):
            queue = deque([node])

            while queue:
                cur = queue.popleft()
                visited.add(cur)
                for nei in adj_list[cur]:
                    if nei not in visited:
                        queue.append(nei)

        
        for node in range(n):
            if node not in visited:
                bfs(node)
                result += 1

        return result
        
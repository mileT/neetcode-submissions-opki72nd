class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_list = {i : [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        queue = deque([0])

        while queue:
            node = queue.popleft()
            if node in visited:
                return False

            visited.add(node)
            for neighbor in adj_list[node]:
                adj_list[neighbor].remove(node)
                queue.append(neighbor)

        return len(visited) == n
        
        # def dfs(node, parent):
        #     if node in visited:
        #         return False
            
        #     visited.add(node)
        #     for neighbor in adj_list[node]:
        #         if neighbor != parent:
        #             if not dfs(neighbor, node):
        #                 return False
        #     return True

        # return dfs(0, -1) and len(visited) == n
        
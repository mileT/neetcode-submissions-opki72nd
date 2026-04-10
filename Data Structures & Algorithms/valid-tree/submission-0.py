class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q = deque([(0, -1)])
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visit:
                    return False
                visit.add(neighbor)
                q.append((neighbor, node))

        return len(visit) == n
        
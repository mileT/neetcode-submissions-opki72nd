class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        pq = [(0, 0)]
        visited = set()
        total_cost = 0

        while len(visited) < n:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            total_cost += cost
            for nei_cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(pq, (nei_cost, nei))

        return total_cost
        
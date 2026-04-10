import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        pq = [(0, 0)]
        visit_set = set()
        total_cost = 0

        while len(visit_set) < n:
            cost, point = heapq.heappop(pq)
            if point in visit_set:
                continue
            visit_set.add(point)
            total_cost += cost

            for nei_cost, nei in adj[point]:
                if nei not in visit_set:
                    heapq.heappush(pq, (nei_cost, nei))

        return total_cost
        
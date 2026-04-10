class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF] * n for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append([v, cost])

        dist[src][0] = 0
        minHeap = [(0, src, -1)] # (cost, node, steps)
        while minHeap:
            cost, node, steps = heapq.heappop(minHeap)
            if node == dst:
                return cost
            if steps == k or dist[node][steps + 1] < cost:
                continue
            for neighbor, weight in adj[node]:
                newCost = cost + weight
                newSteps = steps + 1
                if dist[neighbor][newSteps + 1] > newCost:
                    dist[neighbor][newSteps + 1] = newCost
                    heapq.heappush(minHeap, (newCost, neighbor, newSteps))
        return -1
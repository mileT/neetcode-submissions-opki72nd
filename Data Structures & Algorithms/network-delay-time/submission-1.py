class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        pq = [(k, 0)]

        while pq:
            node, time = heapq.heappop(pq)
            if time > dist[node]:
                continue
            for neighbor, weight in adj[node]:
                if dist[neighbor] > time + weight:
                    dist[neighbor] = time + weight
                    heapq.heappush(pq, (neighbor, dist[neighbor]))

        max_time = max(dist[1:])
        return max_time if max_time != float("inf") else -1        
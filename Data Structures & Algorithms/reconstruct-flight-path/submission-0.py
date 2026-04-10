class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for src, dst in sorted(tickets)[:: -1]:
            adj[src].append(dst)
        route = []
        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())
            route.append(airport)
        dfs("JFK")
        return route[::-1]
        
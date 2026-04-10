class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        n = numCourses
        indegree = [0] * n
        adj = [[] for i in range(n)]

        for start, end in prerequisites:
            indegree[start] += 1
            adj[end].append(start)

        q = deque()
        for course in range(n):
            if indegree[course] == 0:
                q.append(course)

        while q:
            course = q.popleft()
            result.append(course)
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return result if len(result) == n else []
        
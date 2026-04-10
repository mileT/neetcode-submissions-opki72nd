class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        n = numCourses
        adj_list = [[] for i in range(n)]
        indegree = [0] * n

        for a, b in prerequisites:
            adj_list[b].append(a)
            indegree[a] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            result.append(course)
            for nei in adj_list[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return result if len(result) == n else []
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for start, end in prerequisites:
            indegree[end] += 1
            adj[start].append(end)

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                        
        return finish == numCourses
        
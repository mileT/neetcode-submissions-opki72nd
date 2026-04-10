class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adjList = {i : [] for i in range(n)}
        indegrees = [0] * n
        queue = deque([])
        numFinished = 0

        for course, pre in prerequisites:
            adjList[pre].append(course)
            indegrees[course] += 1

        for course in range(n):
            if indegrees[course] == 0:
                queue.append(course)

        while queue:
            node = queue.popleft()
            numFinished += 1
            for nei in adjList[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)

        return numFinished == n
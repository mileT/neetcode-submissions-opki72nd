class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # corner cases check
        if not prerequisites or len(prerequisites) == 0:
            return True

        # model the problem as graph
        indegrees = [0] * numCourses
        graph = [[] for i in range(numCourses)]
        for start, end in prerequisites:
            graph[end].append(start)
            indegrees[start] += 1

        q = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        finished = 0
        while q:
            node = q.popleft()
            finished += 1
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

        return finished == numCourses


        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        n = numCourses
        adj_list= {i : [] for i in range(n)}
        indegree = [0] * n

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            indegree[course] += 1

        queue = deque()
        for course in range(n):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return result if len(result) == n else []

        

        
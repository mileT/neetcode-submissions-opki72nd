class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if preMap[node] == []:
                return True
            
            visiting.add(node)
            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            visiting.remove(node)
            preMap[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
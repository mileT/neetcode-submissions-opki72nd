class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to its prerequisites
        preMap = {i : [] for i in range(numCourses)}
        for cur, pre in prerequisites:
            preMap[cur].append(pre)

        # store all courses along the current DFS path
        visited = set()
        
        def dfs(cur):
            if cur in visited:
                return False
            if preMap[cur] == []:
                return True

            visited.add(cur)
            for pre in preMap[cur]:
                if not dfs(pre):
                    return False
            visited.remove(cur)
            preMap[cur] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
                
        return True
class Solution:
     def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_list = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj_list[pre].append(course)

        order = []
        processed = set()  # Tracks nodes that are fully processed
        has_cycle = False

        def dfs(course, path):
            nonlocal has_cycle
            if course in path:  # Cycle detected
                has_cycle = True
                return
            if course in processed:  # Already processed
                return

            path.add(course)  # Mark as visiting
            for neighbor in adj_list[course]:
                dfs(neighbor, path)
                if has_cycle:
                    return
            path.remove(course)  # Remove after processing
            processed.add(course)
            order.append(course)  # Postorder insertion (reversed topological order)

        for course in range(numCourses):
            if course not in processed:
                dfs(course, set())
                if has_cycle:
                    return []  # Cycle detected, return empty list

        return order[::-1]  # Reverse to get the correct order

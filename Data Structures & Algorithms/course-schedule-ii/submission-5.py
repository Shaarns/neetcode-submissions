class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crs_map = {i: [] for i in range(numCourses)}
        visited, done = set(), set()
        res = []

        #{1: [0], 0: []}
        for crs, pre in prerequisites:
            crs_map[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return []
            
            if crs in done:
                return True

            visited.add(crs)

            for c in crs_map[crs]:
                if not dfs(c): return []

            visited.remove(crs)
            done.add(crs)
            res.append(crs)
            return True

        for crs in crs_map:
            if not dfs(crs): return []

        return res

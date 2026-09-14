class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_req[crs].append(pre)

        visited = set()
        path = set()
        res = []

        def dfs(crs):
            if crs in visited:
                return False

            if crs in path:
                return True

            visited.add(crs)
            for c in pre_req[crs]:
                if not dfs(c):
                    return False

            visited.remove(crs)
            path.add(crs)
            res.append(crs)

            return True

        for crs in pre_req.keys():
            if not dfs(crs):
                return []

        return res
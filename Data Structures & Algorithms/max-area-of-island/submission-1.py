class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        l_row, l_col = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):

            if r < 0 or c < 0 or r >= l_row or c >= l_col:
                return 0

            if grid[r][c] == 0:
                return 0

            if (r, c) in visited:
                return 0

            visited.add((r, c))

            area = 1
            area += dfs(r, c-1)
            area += dfs(r, c+1)
            area += dfs(r+1, c)
            area += dfs(r-1, c)

            return area

        for r in range(l_row):
            for c in range(l_col):
                if grid[r][c] == 1  and (r, c) not in visited:
                    area = dfs(r, c)
                    max_area = max(area, max_area)

        return max_area
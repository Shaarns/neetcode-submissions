class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        l_row, l_col = len(grid), len(grid[0])
        visited = set()
        number_of_island = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= l_row or c >= l_col:
                return

            if grid[r][c] == "0":
                return

            if (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r, c-1)
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r-1, c)

        for r in range(l_row):
            for c in range(l_col):
                if grid[r][c] == "1"  and (r, c) not in visited:
                    number_of_island += 1
                    dfs(r, c)

        return number_of_island
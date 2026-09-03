class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):

            if r < 0 or c < 0 or r >= row_len or c >= col_len:
                return 1

            if grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0


            visited.add((r, c))

            perim = dfs(r, c-1)
            perim += dfs(r, c+1)
            perim += dfs(r-1, c)
            perim += dfs(r+1, c)

            return perim
        
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1 and (r, c) not in visited:
                    return dfs(r,c)

        return 0


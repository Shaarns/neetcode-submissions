class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_of_islands = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0":
                return

            grid[row][col] = "0"
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row-1, col)
            

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_of_islands += 1

        return num_of_islands


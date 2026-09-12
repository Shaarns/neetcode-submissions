class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def add_dis(r, c, distance):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            if grid[r][c] == -1 or grid[r][c] == 0:
                return

            if (r, c) in visited:
                return
            
            visited.add((r, c))
            grid[r][c] = distance
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))


        while q:
            r, c = q.popleft()

            distance = grid[r][c] + 1
            add_dis(r, c+1, distance)
            add_dis(r, c-1, distance)
            add_dis(r+1, c, distance)
            add_dis(r-1, c, distance)
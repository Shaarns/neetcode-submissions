class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        INF = 2147483647

        q = collections.deque()

        def add_visited(r, c, distance):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in visited or grid[r][c] == -1:
                return

            visited.add((r, c))
            grid[r][c] = distance
            q.append((r, c))

        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r, c))

        distance = 1
        while q:
            r, c = q.popleft()

            distance = grid[r][c] + 1

            add_visited(r, c - 1, distance)
            add_visited(r, c + 1, distance)
            add_visited(r + 1, c, distance)
            add_visited(r - 1, c, distance)




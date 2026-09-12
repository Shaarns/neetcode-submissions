class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        minutes = 0

        def add_dis(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            if grid[r][c] != 1:
                return

            if (r, c) in visited:
                return
            
            visited.add((r, c))
            grid[r][c] = 2
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                add_dis(r, c+1)
                add_dis(r, c-1)
                add_dis(r+1, c)
                add_dis(r-1, c)
                
            if q:
                minutes += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minutes
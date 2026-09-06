class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()

        def add(r, c, fresh):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in visited:
                return 0

            if grid[r][c] != 1: return 0
            
            fresh[0] -= 1
            visited.add((r, c))
            q.append([r, c])
            return 1

        fresh = [0]
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh[0] += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        minutes = 0
        while q and fresh[0] > 0:
            time = 0
            for _ in range(len(q)):
                r, c = q.popleft()

                time = max(time, 
                    add(r, c+1, fresh),
                    add(r, c-1, fresh),
                    add(r+1, c, fresh),
                    add(r-1, c, fresh))

            minutes += time


        return minutes if fresh[0] <= 0 else -1

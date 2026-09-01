class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited_path = set()
        
        def backtrack(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or 
                r >= ROW or c >= COL or
                word[i] != board[r][c] or
                (r, c) in visited_path):
                return False

            visited_path.add((r, c))

            res = (backtrack(r, c-1, i+1) or
                backtrack(r, c+1, i+1) or
                backtrack(r+1, c, i+1) or
                backtrack(r-1, c, i+1))

            visited_path.remove((r, c))

            return res
        
        for row in range(ROW):
            for col in range(COL):
                if backtrack(row, col, 0):
                    return True
    
        return False
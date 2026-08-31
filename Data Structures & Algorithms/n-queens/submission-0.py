class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        col = set()
        pos_dia = set() # row+col == same for each diagonals
        neg_dia = set() # row-col == same for each neg diagonals

        def backtrack(row):
            if n == row:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (row+c) in pos_dia or (row-c) in neg_dia:
                    continue

                col.add(c)
                pos_dia.add(row + c)
                neg_dia.add(row - c)

                board[row][c] = 'Q'
                backtrack(row+1)

                col.remove(c)
                pos_dia.remove(row + c)
                neg_dia.remove(row - c)
                board[row][c] = '.'



        backtrack(0)
        return res
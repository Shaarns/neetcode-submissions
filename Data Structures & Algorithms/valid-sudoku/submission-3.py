class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if board[r][c] == '.': continue

                box = (r // 3) * 3 + c//3

                if (board[r][c] in row[r] or
                    board[r][c] in col[c] or 
                    board[r][c] in boxes[box] ):
                    return False

                row[r].add(board[r][c])
                col[c].add(board[r][c])
                boxes[box].add(board[r][c])
        print(row, "row")
        print(col, "col")
        print(boxes, "box")

        return True
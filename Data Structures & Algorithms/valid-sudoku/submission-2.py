class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i, j = 0, 0

        for i in range(len(board)):
            row = set()
            for j in range(len(board)):
                if board[i][j] == '.': continue

                if board[i][j] in row:
                    return False
                else:
                    row.add(board[i][j])

        
        for i in range(len(board)):
            row = set()
            for j in range(len(board)):
                if board[j][i] == '.': continue

                if board[j][i] in row:
                    return False
                else:
                    row.add(board[j][i])
            
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = set()
                for i in range(3):
                    for j in range(3):

                        if board[i + row][j + col] == '.': continue

                        if board[i + row][j + col] in square:
                            return False
                        else:
                            square.add(board[i + row][j + col])

        return True
        


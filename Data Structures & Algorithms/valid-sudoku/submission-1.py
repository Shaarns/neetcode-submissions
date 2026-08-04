class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for m in range(len(board)):
            obj = {}
            for n in range(len(board[0])):
                if(board[m][n] == '.'): continue

                if(board[m][n] in obj):
                    print(obj)
                    return False
                else:
                    obj[board[m][n]] = 1
        
        for m in range(len(board)):
            obj = {}
            for n in range(len(board[0])):
                if(board[n][m] == '.'): continue

                if(board[n][m] in obj):
                    print(obj)
                    return False
                else:
                    obj[board[n][m]] = 1

        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = {}

                for i in range(3):
                    for j in range(3):
                        value = board[row + i][col + j]

                        if value == '.': continue

                        if value in seen:
                            return False
                        seen[value] = 1


        return True

class Solution:
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        curr = self.trie

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["."] = True


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.addWord(word)

        res = set()
        ROW, COL = len(board), len(board[0])
        visited_path = set()
        
        def backtrack(r, c, child_dict, word):
            if (r < 0 or c < 0 or 
                r >= ROW or c >= COL or
                (r, c) in visited_path or 
                board[r][c] not in child_dict):
                return

            visited_path.add((r, c))

            child_dict = child_dict[board[r][c]]
            word += board[r][c]
            if "." in child_dict:
                res.add(word)

            backtrack(r, c-1, child_dict, word)
            backtrack(r, c+1, child_dict, word)
            backtrack(r+1, c, child_dict, word)
            backtrack(r-1, c, child_dict, word)

            visited_path.remove((r, c))
        
    
        for row in range(ROW):
            for col in range(COL):
                backtrack(row, col, self.trie, "")

        return list(res)
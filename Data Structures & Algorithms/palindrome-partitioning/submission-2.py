class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def backtrack(i):
            if i >= len(s):
                res.append(sol.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j, s):
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()

        def is_palindrome(l, r, s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        backtrack(0)
        return res
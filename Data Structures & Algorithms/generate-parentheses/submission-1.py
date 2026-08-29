class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def dfs(openn, close):
            if openn == n and close == n:
                res.append("".join(sol))
                return

            if openn > n or close > n:
                return

            if openn < n:
                sol.append("(")
                dfs(openn+1, close)
                sol.pop()

            if close < n and close < openn:
                sol.append(")")
                dfs(openn, close+1)
                sol.pop()

        dfs(0, 0)
        return res
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def f(m):
            if m in memo:
                return memo[m]
            else:
                memo[m] = f(m-1) + f(m-2)
                return memo[m]

        return f(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2, 3: 3}

        def dp(n):
        
            if n in cache:
                return cache[n]

            cache[n] = dp(n-1) + dp(n-2)
            return cache[n]

        return dp(n)
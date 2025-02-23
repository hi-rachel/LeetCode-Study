class Solution:
    def climbStairs(self, n: int, memo: dict = {}) -> int:
        if n not in memo:
            if n < 3:
                return n
            memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return memo[n]
"""
정수 n이 주어졌을 때, 0부터 n까지의 모든 수에 대해 각 수를 이진수로 표현했을 때 1의 개수를 구하는 문제

TC: O(N)
SC: O(N)
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

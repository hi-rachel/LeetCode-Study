"""
아래로 이동 혹은 (1, 0)
오른쪽 이동만 가능 (0, 1)

m => rows, n = cols
로봇이 (0, 0)에서 (m-1, n-1)에 도착 가능한 unique paths 개수를 반환
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * n for _ in range(m)]
        paths[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
                else:
                    paths[i][j] = 1

        return paths[m - 1][n - 1]

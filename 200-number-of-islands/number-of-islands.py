from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        rows = len(grid)
        cols = len(grid[0])

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            grid[x][y] = 2

            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] == "1":
                            grid[nx][ny] = "2"
                            queue.append((nx, ny))

            return True

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    if bfs(i, j):
                        ans += 1

        return ans

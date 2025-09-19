"""
다음 칸의 고도 ≥ 현재 칸의 고도인 칸들로만 이동

태평양 경계(상단 행 + 좌측 열)에서 출발해 역방향으로 도달 가능한 칸 집합 = pac
대서양 경계(하단 행 + 우측 열)에서 출발해 역방향으로 도달 가능한 칸 집합 = atl
pac ∩ atl
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(starts):
            visited = [[False] * n for _ in range(m)]
            q = deque()

            for r, c in starts:
                if not visited[r][c]:
                    visited[r][c] = True
                    q.append((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        if heights[nr][nc] >= heights[r][c]:
                            visited[nr][nc] = True
                            q.append((nr, nc))

            return visited

        pac_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atl_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]

        pac = bfs(pac_starts)
        atl = bfs(atl_starts)

        res = [[r, c] for r in range(m) for c in range(n) if pac[r][c] and atl[r][c]]
        return res

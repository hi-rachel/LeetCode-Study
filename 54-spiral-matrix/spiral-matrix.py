# 2개의 포인터만 사용하는 풀이
"""
- 위쪽 행을 순회한 후, 열 인덱스를 1씩 증가
- 오른쪽 열을 순회한 후, 행 인덱스를 1씩 증가
- 아래쪽 행을 순회한 후, 열 인덱스를 1씩 감소
- 왼쪽 열을 순회한 후, 행 인덱스를 1씩 감소

인덱스
시작: (0, -1) => 위쪽 행부터 시작하면 (0, 0) => ...
=> (행, 열) => (len(matrix), len(matrix[0]))

탈출 조건
1. 위쪽 행 순회를 마치고 상단 인덱스가 하단 인덱스보다 커지면
2. 오른쪽 열 순회를 마치고, 우측 인덱스가 좌측 인덱스보다 작아지면
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n_rows, n_cols = len(matrix), len(matrix[0])
        row, col = 0, -1
        direction = 1

        output = []

        # 남아있는 열과 행의 개수가 0 보다 큰 동안
        while 0 < n_rows and 0 < n_cols:
            for _ in range(n_cols):
                col += direction
                output.append(matrix[row][col])
            n_rows -= 1

            for _ in range(n_rows):
                row += direction
                output.append(matrix[row][col])
            n_cols -= 1

            direction *= -1

        return output
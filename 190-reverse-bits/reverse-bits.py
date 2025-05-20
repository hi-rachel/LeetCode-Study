"""
1. 입력받은 정수 n을 32비트 이진수로 바꾼다
2. 이진수를 좌우로 뒤집는다 -> stack 활용
2. 뒤집은 이진수의 정수값을 반환한다

항상 32비트이므로 상수 시간, 상수 공간
TC: O(1)
SC: O(1)
"""

# 비트 연산자 풀이
class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []
        while len(stack) < 32:
            stack.append(n & 1)  # 마지막 비트 1이면 1, 0이면 0
            n >>= 1  # %= 2 와 같은 효과, 오른쪽 쉬프트

        output, scale = 0, 1  # 결과, 2^0 = 1 시작
        while stack:
            output += stack.pop() * scale
            scale <<= 1  # *= 2 와 같은 효과

        return output

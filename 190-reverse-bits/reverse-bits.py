"""
1. 입력받은 정수 n을 32비트 이진수로 바꾼다
2. 이진수를 좌우로 뒤집는다 -> stack 활용
2. 뒤집은 이진수의 정수값을 반환한다

항상 32비트이므로 상수 시간, 상수 공간
TC: O(1)
SC: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "032b")[::-1], 2)

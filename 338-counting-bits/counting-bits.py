"""
정수 n이 주어졌을 때, 0부터 n까지의 모든 수에 대해 각 수를 이진수로 표현했을 때 1의 개수를 구하는 문제
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOne(num):
            cnt = 0
            while True:
                rest = num % 2
                if rest == 1:
                    cnt += 1
                num //= 2
                if num <= 1:
                    if num == 1:
                        cnt += 1
                    break
            return cnt

        result = []
        for i in range(0, n + 1):
            result.append(countOne(i))

        return result
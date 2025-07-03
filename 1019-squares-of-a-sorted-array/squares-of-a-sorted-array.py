"""
각 숫자의 제곱을 오름차순으로 반환해라
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            answer.append(num * num)

        answer.sort()
        return answer
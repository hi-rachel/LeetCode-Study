"""
오름차순 nums 배열이 주어졌을 때,
각 숫자의 제곱을 오름차순으로 반환해라

문제 풀이
- 가장 큰 제곱값은 양 끝에 위치한 숫자 중 절대값이 큰 값에서 나온다
=> 투 포인터 활용

TC: O(n)
SC: O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        left, right = 0, n - 1
        i = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                answer[i] = nums[left] ** 2
                left += 1
            else:
                answer[i] = nums[right] ** 2
                right -= 1
            i -= 1
        return answer
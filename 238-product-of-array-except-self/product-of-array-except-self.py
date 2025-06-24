# 정수 배열 nums가 주어졌을 때,
# 각 인덱스 i에 대해 nums[i]를 제외한 모든 원소의 곱을 담은 배열을 반환
# O(n) 시간 복잡도에 풀어야 함.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # 왼쪽 곱 누적
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # 오른쪽 곱 누적
        right = 1
        for i in reversed(range(n)):
            res[i] *= right
            right *= nums[i]

        return res


"""
nums 배열과 정수 k가 주어졌을 때,
nums 배열 안에 k 길이인 subarray의 평균값이 최대가 되는 값을 구해라
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # k ~ len(nums) - 1
        for i in range(k , len(nums)):
            # 윈도우 이동
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


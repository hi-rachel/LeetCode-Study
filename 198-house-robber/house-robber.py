"""
2가지 선택
1. 이 집을 턴다.
-> i-2까지의 최댓값 + 현재 집

2. 이 집을 안 턴다.
-> i-1까지의 최댓값을 그대로 유지

dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[-1]
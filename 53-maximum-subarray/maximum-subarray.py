class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            total = max(nums[i], total + nums[i])
            max_total = max(total, max_total)
        return max_total 
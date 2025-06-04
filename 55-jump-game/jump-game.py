class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for idx in range(len(nums)):
            if idx <= reach:
                reach = max(reach, idx + nums[idx])
        return len(nums) - 1 <= reach
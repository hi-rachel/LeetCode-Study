"""
1. set()
2. 정렬 O(n log n)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        max_cnt = 1
        cnt = 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1

        return max_cnt
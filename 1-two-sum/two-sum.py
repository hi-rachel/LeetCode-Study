"""
O(N) time, O(N) space
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        
        for i, v in enumerate(nums):
            diff = target - v
            if diff in indices:
                j = indices[diff]
                return [i, j]
            indices[v] = i
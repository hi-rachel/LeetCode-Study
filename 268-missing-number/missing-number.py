class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums)):
            if i not in num_set:
                return i
        return len(nums)
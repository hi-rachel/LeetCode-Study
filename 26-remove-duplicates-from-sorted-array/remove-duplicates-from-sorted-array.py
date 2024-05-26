class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_idx = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_idx]:
                unique_idx += 1
                nums[unique_idx] = nums[i]

        return unique_idx+1
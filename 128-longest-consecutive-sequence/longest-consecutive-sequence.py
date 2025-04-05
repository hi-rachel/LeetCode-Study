class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longest = 0
        cnt = 1

        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                cnt += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                longest = max(cnt, longest)
                cnt = 1
        longest = max(cnt, longest)
        
        return longest
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        nums.sort()
        result = []
        cnt = 1

        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                cnt += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                result.append(cnt)
                cnt = 1
        result.append(cnt)
        
        return max(result)
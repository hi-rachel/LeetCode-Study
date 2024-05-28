class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        prev = 0
        max_num = 0
        for i in range(len(nums)-1):
            max_num = max(max_num, i + nums[i])

            if (prev == i):
                prev = max_num
                cnt += 1
        return cnt
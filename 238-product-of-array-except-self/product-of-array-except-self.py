class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        R = 1 
        for i in reversed(range(n)):
            answer[i] *= R
            R *= nums[i]

        return answer
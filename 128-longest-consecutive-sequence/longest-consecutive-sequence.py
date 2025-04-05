class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        while num_set:
            num = num_set.pop()
            left, right = 1, 1
            while num - left in num_set:
                num_set.remove(num - left)
                left += 1
            while num + right in num_set:
                num_set.remove(num + right)
                right += 1
            longest = max(left + right - 1, longest)
        return longest
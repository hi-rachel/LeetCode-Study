from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = defaultdict(int)

        for num in nums:
            nums_map[num] += 1

        sort_dict = dict(sorted(nums_map.items(), key=lambda item: item[1], reverse=True))

        keys = list(sort_dict)

        return keys[:k]
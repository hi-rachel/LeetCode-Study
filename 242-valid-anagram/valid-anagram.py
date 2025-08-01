from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def makeMap(s: str):
            str_map = defaultdict(int)
            for char in s:
                str_map[char] += 1
            return str_map

        return makeMap(s) == makeMap(t)
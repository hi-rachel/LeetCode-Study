from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for char in s:
            map1[char] += 1
        for char in t:
            map2[char] += 1

        if map1 == map2:
            return True
        else:
            return False
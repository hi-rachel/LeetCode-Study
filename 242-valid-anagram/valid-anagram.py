class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for char in s:
            map1[char] = map1.get(char, 0) + 1
        for char in t:
            map2[char] = map2.get(char, 0) + 1

        if map1 == map2:
            return True
        else:
            return False
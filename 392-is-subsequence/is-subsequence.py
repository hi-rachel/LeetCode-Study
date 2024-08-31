class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) < len(s):
            return False
        now = 0
        end = len(s)
        for i in range(len(t)):
            if t[i] == s[now]:
                now += 1
                if now == end:
                    return True
        return False
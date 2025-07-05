class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for bracket in s:
            if stack and stack[-1] in brackets and brackets[stack[-1]] == bracket:
                stack.pop()
            else:
                stack.append(bracket)
            
        return not stack

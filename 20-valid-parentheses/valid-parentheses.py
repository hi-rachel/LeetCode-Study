class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []

        for char in s:
            if char in '[{(':
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if match[top] != char:
                    return False
        
        return not stack
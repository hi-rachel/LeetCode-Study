class Solution:
    def isValid(self, s: str) -> bool:
        parentheseMap = {")" : "(", "]": "[", "}": "{"}
        stack = []
        open_parenthese = "([{"

        for char in s:
            if char in open_parenthese:
                stack.append(char)
            else:
                if (not stack or stack.pop() != parentheseMap[char]):
                    return False
            
        return len(stack) == 0
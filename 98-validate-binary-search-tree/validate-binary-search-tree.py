"""
모든 왼쪽 서브트리는 현재 노드보다 작아야 하고,
모든 오른쪽 서브트리는 현재 노드보다 커야 한다.

이걸 위해서 범위(min/max)를 재귀로 내려보내야 한다.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))
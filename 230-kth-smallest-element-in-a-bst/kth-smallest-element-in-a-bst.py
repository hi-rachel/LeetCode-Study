# BST에서 k번째로 작은 value를 반환해라
# 인덱스는 1에서 시작

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 풀이 1. Sort
# 모든 노드의 값을 오름차순으로 정렬 후에 k번째 값을 구한다.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            
            values.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return sorted(values)[k-1]
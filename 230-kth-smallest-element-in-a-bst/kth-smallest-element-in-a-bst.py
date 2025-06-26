# BST에서 k번째로 작은 value를 반환해라
# 인덱스는 1에서 시작

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 풀이 3. 중위 순회 활용
# BST는 중위 순회를 하면 오름차순으로 노드에 접근할 수 있다
# => 입력 트리를 중위 순회 하면서 노드 값을 배열에 저장하면 자연스럽게 배열은 정렬됨

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return values[k - 1]

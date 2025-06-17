# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 둘 다 null이면 True 반환
        if not p and not q:
            return True
        # 둘 중 하나면 null이면 False 반환
        if not p or not q:
            return False
        # val이 서로 다르면 탐색 중단, False 반환
        if p.val != q.val:
            return False
        # 현재 node의 val이 같다면, 좌우측 자식 트리도 같은지 확인 -> 재귀 호출
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

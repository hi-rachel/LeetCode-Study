class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None  # 이전 중위 순회 값

        while stack or root:
            # 왼쪽 끝까지 탐색
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # 이전 값보다 작거나 같으면 BST 위반
            if prev is not None and root.val <= prev:
                return False
            prev = root.val

            # 오른쪽으로 이동
            root = root.right

        return True
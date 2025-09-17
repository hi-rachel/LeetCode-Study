# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            # 해당 노드 이미 방문한 적 있으면
            if head in visited:
                return True
            # 방문한 적 없으면 set에 넣기
            visited.add(head)
            # 다음 노드로 이동
            head = head.next

        # cycle이 없음
        return False
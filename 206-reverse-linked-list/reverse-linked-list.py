# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # 이전 노드
        curr = head  # 현재 노드

        while curr:
            next_node = curr.next  # 다음 노드 기억
            curr.next = prev       # 현재 노드의 방향을 반대로
            prev = curr            # 이전 노드를 한 칸 앞으로
            curr = next_node       # 현재 노드를 다음으로 이동

        # prev가 마지막 노드이자 새 head
        return prev
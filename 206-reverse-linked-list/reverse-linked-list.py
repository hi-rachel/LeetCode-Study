# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            stack.append(node)
            node= node.next

        dummy = ListNode(-1)
        node = dummy
        while stack:
            node.next = stack.pop()
            node = node.next
        node.next = None
        return dummy.next
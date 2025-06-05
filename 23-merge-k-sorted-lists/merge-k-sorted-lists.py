# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for li in lists:
            while li:
                nums.append(li.val)
                li = li.next

        dummy = curr = ListNode(-1)
        for num in sorted(nums):
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
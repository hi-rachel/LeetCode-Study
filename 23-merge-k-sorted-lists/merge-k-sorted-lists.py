# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Step 1. 각 리스트의 첫 노드를 heap에 넣음 (val, 고유번호, 노드)
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        dummy = curr = ListNode(-1)

        # Step 2. heap에서 가장 작은 값 꺼내면서 결과 리스트 구성
        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                # 다음 노드를 힙에 추가
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next
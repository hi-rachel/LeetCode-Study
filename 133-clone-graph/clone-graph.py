"""
무방향 연결된 노드
그래프의 깊은 복사 반환해라

TC: O(V + E) V: 노드의 수, E: 이웃의 수
SC: O(V + E)

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        clone = Node(node.val)
        clones = {node: clone}
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for nei in node.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    queue.append(nei)
                clones[node].neighbors.append(clones[nei])
        return clone

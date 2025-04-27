from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(0, 0)])
        visited = set()
        while queue:
            count, total = queue.popleft()
            if total == amount:
                return count
            if total in visited:
                continue
            visited.add(total)
            for coin in coins:
                if total + coin <= amount:
                    queue.append((count + 1, total + coin))
        return - 1
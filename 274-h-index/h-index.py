class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cnt = 0
        citations.sort(reverse=True)
        print(citations)
        for idx, paper in enumerate(citations):
            if paper >= idx + 1:
                cnt += 1
            
        return cnt
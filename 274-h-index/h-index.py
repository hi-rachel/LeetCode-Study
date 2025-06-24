# 내림차순 정렬 후, 앞에서부터 'i번째 논문이 i + 1번 이상 인용됐는가?' 체크
# 
# TC: O(n log n)
# SC: O(1)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cnt = 0
        citations.sort(reverse=True)

        for idx, paper in enumerate(citations):
            if paper >= idx + 1:
                cnt += 1
            
        return cnt
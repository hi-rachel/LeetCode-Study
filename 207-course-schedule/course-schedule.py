"""
문제: 수강 해야 하는 모든 강좌의 수 numCourses가 주어질 때, 모든 강좌를 끝낼 수 있으면 true, 아니면 false를 반환해라.
     prerequisites[i] = [ai, bi], bi를 수강하기 위해선 반드시 ai를 사전 수강해야만 한다.
     numCourses courses labeled from 0 to numCourses - 1
     0 <= ai, bi < numCourses


TC: O(V + E), V: 과목 수, E: prerequisite 관계 수
SC: O(V + E), 그래프 + 진입차수 배열
"""

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # 1. 그래프 만들기, 2. 진입차수 계산
        # 수강 강의, 사전 강의
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # 3. Queue에 진입 차수가 0인 노드부터 넣고 시작
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0

        # 4. BFS 탐색, 처리된 노드 수가 전체 강의 수와 같으면 True, 아니면 False
        while queue:
            # queue에서 꺼낸 과목을 수강 완료 처리
            current = queue.popleft()
            completed += 1

            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            
        return completed == numCourses

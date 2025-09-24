class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        traversing = set()

        @cache
        def can_finish(crs):
            if crs in traversing:
                return False
            
            traversing.add(crs)
            result = all(can_finish(pre) for pre in graph[crs])
            traversing.remove(crs)
            return result

        return all(can_finish(crs) for crs in graph)

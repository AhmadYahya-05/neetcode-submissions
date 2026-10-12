class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        visit = set()
        
        for course,prereq in prerequisites:
            preMap[course].append(prereq)
        
        def dfs(course):

            if course in visit:
                return False

            if preMap[course] == []:
                return True

            visit.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
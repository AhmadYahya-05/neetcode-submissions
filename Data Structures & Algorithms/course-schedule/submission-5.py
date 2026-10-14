class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # for each course use adjency list to map its prereqs: 
        # use a set for cycle detection
        # use dfs 

        adj_list = {i: [] for i in range(numCourses)}
        visit = set()
        
        for course,prereq in prerequisites:
            adj_list[course].append(prereq)

        def dfs(i):
            
            if i in visit:
                return False
            if adj_list[i] == []:
                return True 

            visit.add(i)
            for node in adj_list[i]:
                if not dfs(node):
                    return False
            visit.remove(i)
            adj_list[i] = []
        
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
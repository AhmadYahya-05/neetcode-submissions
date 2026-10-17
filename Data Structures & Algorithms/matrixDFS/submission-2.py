class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        visited = set()
        count = 0

        def dfs (r,c):

            if min(r,c) < 0 or r >= rows or c >= cols:
                return 0

            if grid[r][c] == 1 or (r,c) in visited:
                return 0

            if r == rows - 1 and c == cols - 1 and grid[r][c] == 0:
                return 1
            
            visited.add((r,c))
            count = sum((dfs(r+1,c),dfs(r-1,c),dfs(r,c+1),dfs(r,c-1)))
            visited.remove((r,c))
            return count 
        
        return dfs(0,0)
        


        
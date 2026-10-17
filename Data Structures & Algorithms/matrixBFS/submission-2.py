class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        visited = set()
        q = deque()
        r,c = 0,0
        q.append((r,c))

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        length = -1
        visited.add((0,0))
        
        while q:
            length += 1                     
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length            
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))

        return -1 


    
            

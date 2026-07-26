class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        result = [[float("inf")] * (cols + 1) for r in range(rows +1)]
        result[rows -1][cols] = 0

        for r in range (rows -1, -1, -1):
            for c in range (cols -1, -1, -1):
                result[r][c] = grid[r][c] + min(result[r][c+1], result[r+1][c])
            
        return result[0][0]

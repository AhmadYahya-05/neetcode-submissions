class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # use recursion to determine if theres a path 

        rows, cols = len(board),len(board[0])
        visited = set()

        def dfs(r,c,i):
            if i == len(word): return True
            
            if min(r,c) < 0 or r >= rows or c >= cols:
                return False

            if (r,c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r,c))
            true = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) 
            or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            visited.remove((r,c))
            return true

        found = False
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    found = True

        return found
                


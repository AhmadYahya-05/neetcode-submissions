class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows,cols = len(board),len(board[0])
        visited = set()
        i = 0

        def dfs(r,c,i,current_string):

            if min(r,c) < 0 or r >= rows or c >= cols:
                return False

            if (r,c) in visited or board[r][c] not in word[i]:
                return False

            current_string += (board[r][c])
            visited.add((r,c))
            
            if current_string == word:
                return True 
            
            found = (dfs(r+1,c,i+1,current_string) or
            dfs(r-1,c,i+1,current_string) or
            dfs(r,c+1,i+1,current_string) or
            dfs(r,c-1,i+1,current_string))
            
            visited.remove((r,c))
            return found 
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0,current_string = ''):
                    return True 
        return False

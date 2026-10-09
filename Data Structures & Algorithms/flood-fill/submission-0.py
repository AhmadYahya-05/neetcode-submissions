class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        og_color = image[sr][sc]
        
        r = len(image)
        c = len(image[0])
        visited = set()
        
        if color == og_color:
            return image

    
        def dfs(sr,sc): 

            if min(sr,sc) < 0 or sr >= r or sc >= c:
                return

            if (sr,sc) in visited:
                return 
            
            if image[sr][sc] != og_color:
                return


            visited.add((sr,sc))
            image[sr][sc] = color

            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)

        dfs(sr,sc)
        return image


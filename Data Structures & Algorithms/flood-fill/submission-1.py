class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])
        visited = set()
        og_color = image[sr][sc]
        
        def dfs(sr,sc):

            if min(sr,sc) < 0 or sr >= rows or sc >= cols:
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

            visited.remove((sr,sc))
            return image

        return dfs(sr,sc)


            

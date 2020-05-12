class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        h, w = len(image), len(image[0])
        src_color = image[sr][sc]
        visited = set()
        def dfs( r, c):
            if r < 0 or c < 0 or r >= h or c >= w or (r,c) in visited or image[r][c] != src_color:
                return
            image[r][c] = newColor
            visited.add( (r,c) )
            dfs( r-1, c)
            dfs( r+1, c)
            dfs( r, c-1 )
            dfs( r, c+1)
        
        dfs(sr, sc)
        
        return image
        

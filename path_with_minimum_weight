#compue minimum weight of a path from top left corner to bottom right when each square of the grid has a weight
#leetcode exercise: https://leetcode.com/problems/minimum-path-sum/?envType=problem-list-v2&envId=dynamic-programming
#memory used: n*m, time complexity: n*m

def minPathSum(self, grid: List[List[int]]) -> int:
    m=len(grid)
    n=len(grid[0])
    paths=[[0]*n for j in range(m)]
    paths[m-1][n-1]=grid[m-1][n-1]
    for k in range(1,m):
        paths[m-1-k][n-1]=paths[m-1-k+1][n-1]+grid[m-1-k][n-1]
    for k in range(1,n):
        paths[m-1][n-1-k]=paths[m-1][n-k+1-1]+grid[m-1][n-1-k]    
    for j in range(1,n):
        for k in range(1,m):
            paths[m-1-k][n-1-j]=min(paths[m-k][n-1-j],paths[m-1-k][n-j])+grid[m-1-k][n-1-j]
    return paths[0][0]

grid = [[1,3,1],[1,5,1],[4,2,1]]
m, n = len(grid), len(grid[0])
for i in range(1, m):
    grid[i][0] += grid[i-1][0]
print(grid)
for i in range(1, n):
    grid[0][i] += grid[0][i-1]
print(grid)
for i in range(1, m):
    for j in range(1, n):
        grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        print(grid)
print(grid)
print(grid[i][j])

i = open("D:\CSE221\Lab5\input6_3.txt",'r')
o = open("D:\CSE221\Lab5\output6.txt",'w')

row_column = i.readline().split()
row = int(row_column[0])
column = int(row_column[1])

dora_map = []
for k in i.readlines():
    dora_map.append(k)

def flood_fill(grid, visited, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return 0
    if visited[row][col] or grid[row][col] == '#':
        return 0
    visited[row][col] = True
    if grid[row][col] == 'D':
        diamonds = 1 
    else:
        diamonds = 0
    diamonds += flood_fill(grid, visited, row+1, col)
    diamonds += flood_fill(grid, visited, row-1, col)
    diamonds += flood_fill(grid, visited, row, col+1)
    diamonds += flood_fill(grid, visited, row, col-1)
    return diamonds

def max_diamonds(grid):
    max_diamonds = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'D':
                visited = [[False]*len(grid[0]) for _ in range(len(grid))]
                diamonds = flood_fill(grid, visited, row, col)
                max_diamonds = max(max_diamonds, diamonds)
    return max_diamonds

o.write(str(max_diamonds(dora_map)))

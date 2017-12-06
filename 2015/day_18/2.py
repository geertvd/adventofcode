import copy

def get_neighbours_on(grid, x, y):
    neighbours_on = 0
    for xx in range(max(x-1, 0), min(x+2, len(grid))):
        for yy in range(max(y-1, 0), min(y+2, len(grid[x]))):
            if (xx != x or yy != y) and grid[xx][yy]:
                neighbours_on += 1
    return neighbours_on

lines = file('grid.txt').readlines();
grid = [[0 for x in range(len(lines))] for x in range(len(lines[0].strip()))]
for x, line in enumerate(lines):
    line = line.strip()
    for y, char in enumerate(line):
        grid[x][y] = 1 if char == '#' else 0

for i in range(100):
    new_grid = copy.deepcopy(grid)
    for x, row in enumerate(grid):
        for y, state in enumerate(row):
            neighbours_on = get_neighbours_on(grid, x, y)
            if state and neighbours_on in [2, 3]:
                new_grid[x][y] = 1
            elif not state and neighbours_on == 3:
                new_grid[x][y] = 1
            else:
                new_grid[x][y] = 0
    new_grid[0][0] = 1
    new_grid[len(grid) - 1][0] = 1
    new_grid[0][len(grid[0]) - 1] = 1
    new_grid[len(grid) - 1][len(grid[0]) - 1] = 1
    grid = new_grid
print sum(x.count(1) for x in grid)
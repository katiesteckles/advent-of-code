import copy

with open("2021/day11_input.txt", "r") as file:
    input = file.readlines()
    input = [list(map(int,line.strip())) for line in input]

with open("2021/day11_test.txt", "r") as file:
        testinput = file.readlines()
        testinput = [list(map(int,line.strip())) for line in testinput]

def find_neighbour_spaces(grid, x, y):
    if x > len(grid[0]) or y > len(grid):
        return 'Out of range'
    #print('Point: ('+str(x)+', '+str(y)+')')
    neighbour_spaces = set()
    if x > 0:
        neighbour_spaces.add((x - 1, y))
        if y > 0:
            neighbour_spaces.add((x - 1, y - 1))
    if x < len(grid[0]) - 1:
        neighbour_spaces.add((x + 1, y))
        if y < len(grid) - 1:
            neighbour_spaces.add((x + 1, y + 1))
    if y > 0:
        neighbour_spaces.add((x, y - 1))
        if x < len(grid[0]) - 1:
            neighbour_spaces.add((x + 1, y - 1))
    if y < len(grid) - 1:
        neighbour_spaces.add((x, y + 1))
        if x > 0:
            neighbour_spaces.add((x - 1, y + 1))
    #print('Neighbours: '+str(neighbour_spaces))
    return neighbour_spaces


def iterate_step(grid):
    grid_iteration = copy.deepcopy(grid)
    # print('\n'.join(' '.join(map(str, sub)) for sub in grid_iteration))
    flashes = set()
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            grid_iteration[y][x] += 1
    flashes_now = -1
    while len(flashes) - flashes_now != 0:
        flashes_now = len(flashes)
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid_iteration[y][x] > 9 and (x,y) not in flashes:
                    flashes.add((x, y))
                    for neighbour in find_neighbour_spaces(grid_iteration, x, y):
                        grid_iteration[neighbour[1]][neighbour[0]] += 1
    for flash in flashes:
        grid_iteration[flash[1]][flash[0]] = 0
    return grid_iteration, flashes

grids = [[input, set()]]
for i in range(100):
    grids.append(list(iterate_step(grids[-1][0])))

flash_total = 0
for grid in grids:
    flash_total += len(grid[1])

# part 2

for i in range(200):
    grids.append(list(iterate_step(grids[-1][0])))
    if len(grids[-1][1]) == 100:
        print(i+201)
        break
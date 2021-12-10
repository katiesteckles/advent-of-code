import copy

with open("2021/day09_input.txt", "r") as file:
    input = file.readlines()
    input = [list(map(int, line[:-1])) for line in input]

test_raw = ['2199943210', '3987894921', '9856789892', '8767896789', '9899965678']
test_data = [list(map(int, testline)) for testline in test_raw]


def find_neighbours(grid, x, y):
    if x > len(grid[0]) or y > len(grid):
        return 'Out of range'
    neighbours = [grid[y][x]]
    if x > 0:
        neighbours.append(grid[y][x - 1])
    if x < len(grid[0]) - 1:
        neighbours.append(grid[y][x + 1])
    if y > 0:
        neighbours.append(grid[y - 1][x])
    if y < len(grid) - 1:
        neighbours.append(grid[y + 1][x])
    return neighbours  # the point itself, right, left, up, down


# find_neighbours(test_data, 1,1)

def is_minimum(neighb_set):
    if neighb_set == 'Out of range':
        return neighb_set
    for neighbour in neighb_set[1:]:
        # print(neighbour)
        if neighb_set[0] >= neighbour:
            return False
    return True


def find_local_minima_risk(grid):
    local_minima_risk = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if is_minimum(find_neighbours(grid, x, y)):
                local_minima_risk += find_neighbours(grid, x, y)[0] + 1
    return local_minima_risk

print(find_local_minima_risk(input))

# part 2

def find_neighbour_spaces(grid, x, y):
    if x > len(grid[0]) or y > len(grid):
        return 'Out of range'
    neighbour_spaces = [[x, y]]
    if x > 0:
        neighbour_spaces.append([x-1, y])
    if x < len(grid[0]) - 1:
        neighbour_spaces.append([x + 1, y])
    if y > 0:
        neighbour_spaces.append([x, y - 1])
    if y < len(grid) - 1:
        neighbour_spaces.append([x, y + 1])
    return neighbour_spaces  # the point itself, right, left, up, down

print(find_neighbour_spaces(input,0, 5))

def find_basin(grid, x, y):
    basin = set()
    if grid[y][x] == 9:
        return basin
    basin.add((x,y))
    found_new_points = True
    while found_new_points == True:
        new_neighbours = set()
        for point in basin:
            new_neighbours = new_neighbours | non_nine_neighbours(grid, point[0], point[1])
        if len(new_neighbours ^ basin) == 0:
            found_new_points = False
        basin = basin | new_neighbours
    return basin

def non_nine_neighbours(grid, x, y):
    nnns = set()
    neighbour_spaces = find_neighbour_spaces(grid, x, y)
    for space in neighbour_spaces[1:]:
        if grid[space[1]][space[0]] != 9:
            nnns.add((space[0],space[1]))
    return nnns

def find_all_basins(grid):
    basins = set()
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            basins.add(frozenset(find_basin(grid, x, y)))
    return basins

basins = find_all_basins(input)

setlengths = sorted([len(basin) for basin in basins])
product = setlengths[-1]*setlengths[-2]*setlengths[-3]
print(product)

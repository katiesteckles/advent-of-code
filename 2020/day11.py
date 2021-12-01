import copy
with open("day11_input.txt", "r") as file:
    rows = file.readlines()

the_grid = [row[:-1] for row in rows]
the_test_grid = ['L.LL.LL.LL','LLLLLLL.LL','L.L.L..L..','LLLL.LL.LL','L.LL.LL.LL','L.LLLLL.LL','..L.L.....','LLLLLLLLLL','L.LLLLLL.L','L.LLLLL.LL']

def get_nbhd(x, y, grid):
    return [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]]

def get_long_nbhd(x,y,gridwidth,gridheight):
    long_nbhd = [
                [[x, y-i-1] for i in range(y)], # straight up
                [[x+i+1, y-j-1] for i, j in zip(range(gridwidth-x-1), range(y))],  # up and right
                [[x+i+1, y] for i in range(gridwidth-x-1)], # to the right
                [[x+i+1, y+j+1] for i,j in zip(range(gridwidth-x-1), range(gridheight-y-1))], # down and right
                [[x, y+i+1] for i in range(gridheight-y-1)], # to the bottom
                [[x-i-1, y+j+1] for i, j in zip(range(x), range(gridheight-y-1))],  # down and left
                [[x-i-1, y] for i in range(x)], # to the left
                [[x-i-1, y-j-1] for i,j in zip(range(x), range(y))] # up and left
                ]
    return long_nbhd

def look_around_you(x,y,grid):
    long_nbhd = get_long_nbhd(x,y,len(grid[0]),len(grid))
    nbhd = []
    for direction in long_nbhd:
        for seat in direction:
            if grid[seat[1]][seat[0]] != '.':
                nbhd.append([seat[0],seat[1]])
                break
    return nbhd

# sample: minesweeper_the_thing(the_grid,'#',get_nbhd):
def minesweeper_the_thing(grid,thing_to_count,nbhd_fn):
    grid_of_counts = []
    for y in range(len(grid)):
        this_row = []
        for x in range(len(grid[y])):
            count_so_far = 0
            nbhd_xy = nbhd_fn(x,y,grid)
            for pair in nbhd_xy:
                if pair[1] in range(len(grid)) and pair[0] in range(len(grid[y])) and grid[pair[1]][pair[0]] == thing_to_count:
                    count_so_far +=1
            this_row.append(count_so_far)
        grid_of_counts.append(this_row)
    return grid_of_counts

# for this game: live_min = 0, live_max = 0; die_min = 4,  die_max = 8
def iterate_the_grid(grid, live_min, live_max, die_min, die_max, nbhd_fn):
    grid_of_counts = minesweeper_the_thing(grid, '#', nbhd_fn)
    new_grid = []
    for y in range(len(grid)):
        this_row = []
        #print('Current row: ' + str(grid[y]))
        #print('Counts for this row: ' + str(grid_of_counts[y]))
        for x in range(len(grid[y])):
            if grid[y][x] == 'L' and live_min <= grid_of_counts[y][x] <= live_max:
                new_symbol = '#'
            elif grid[y][x] == '#' and die_min <= grid_of_counts[y][x] <= die_max:
                new_symbol = 'L'
            else:
                new_symbol = grid[y][x]
            this_row.append(new_symbol)
        #print('New row: ' + str(''.join(this_row)))
        new_grid.append(''.join(this_row))
    return new_grid

oldgrid = copy.deepcopy(the_grid)
#oldgrid = copy.deepcopy(the_test_grid)
newgrid = iterate_the_grid(oldgrid,0,0,5,8, look_around_you)
while newgrid != oldgrid:
    newnewgrid = iterate_the_grid(newgrid,0,0,5,8, look_around_you)
    oldgrid = newgrid
    newgrid = newnewgrid

total_hashes = 0
for row in newgrid:
    total_hashes += row.count('#')


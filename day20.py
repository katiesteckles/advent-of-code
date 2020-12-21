import copy
with open("day20_input.txt", "r") as file:
    input = file.read()

input = input.replace('.','@')

tiles = input.split('\n\n')
tiles = [tile.split('\n') for tile in tiles]
tiles = [[tile[0][5:9], tile[1:]] for tile in tiles]

def print_grids(grid1, grid2):
    print('Original:     Transformed:')
    for i in range(len(grid1)):
        print(str(grid1[i][0]) + str(grid1[i][1]) + str(grid1[i][2]) + str(grid1[i][3]) + str(grid1[i][4]) + str(grid1[i][5]) + str(grid1[i][6]) + str(grid1[i][7]) + str(grid1[i][8]) + str(grid1[i][9]) +  '    ' + str(grid2[i][0]) + str(grid2[i][1]) + str(grid2[i][2]) + str(grid2[i][3]) + str(grid2[i][4])+ str(grid2[i][5])+ str(grid2[i][6])+ str(grid2[i][7])+ str(grid2[i][8])+ str(grid2[i][9]))

print_grids(tiles[0][1], tiles[1][1])

# write a function to do all the rotating and reflecting

def tile_transform(tile_grid,orientation): # should be a 10 by 10 grid, fed in as a list of 10 strings of length 10
    transformed_grid = copy.deepcopy(tile_grid)
    rows = len(transformed_grid)
    cols = len(transformed_grid[0]) # these should both be 10
    if orientation == 1: # first row l-r becomes last column t-b
        for i in range(rows):
            row_i = ''
            for j in range(cols):
                row_i += tile_grid[cols-1-j][i]
            transformed_grid[i] = row_i
    elif orientation == 2: # first row l-r becomes bottom row r-l
        for i in range(rows): # goes through the rows
            transformed_grid[rows-1-i] = tile_grid[i][::-1]
    elif orientation == 3: # first row l-r becomes first column b-t
        for i in range(rows):
            row_i = ''
            for j in range(cols):
                row_i += tile_grid[j][cols - 1 - i]
            transformed_grid[i] = row_i
    elif orientation == 4:
        transformed_grid = [row[::-1] for row in tile_grid]
    elif orientation == 5:
        for i in range(rows):
            row_i = ''
            for j in range(cols):
                row_i += tile_grid[rows-1-j][cols-1-i]
            transformed_grid[i] = row_i
    elif orientation == 6: # first row l-r becomes bottom row l-r
        for i in range(rows): # goes through the rows
            transformed_grid[i] = tile_grid[rows-1-i]
    elif orientation == 7:
        for i in range(rows):
            row_i = ''
            for j in range(cols):
                row_i += tile_grid[j][i]
            transformed_grid[i] = row_i
    print_grids(tile_grid, transformed_grid)
    return transformed_grid

tile_transform(tiles[0][1],7)

# generate all the grids and put them in a big list of lists of grids under the same heading
# do the thing Paul said where you do a backtracking search
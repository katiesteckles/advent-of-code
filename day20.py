import copy
with open("day20_input.txt", "r") as file:
    input = file.read()

input = input.replace('.','@')

tiles = input.split('\n\n')
tiles = [tile.split('\n') for tile in tiles]
tiles = [[tile[0][5:9], tile[1:]] for tile in tiles[:-1]]

def print_grids(grid1, grid2):
    print('Original:     Transformed:')
    for i in range(len(grid1)):
        print(str(grid1[i][0]) + str(grid1[i][1]) + str(grid1[i][2]) + str(grid1[i][3]) + str(grid1[i][4]) + str(grid1[i][5]) + str(grid1[i][6]) + str(grid1[i][7]) + str(grid1[i][8]) + str(grid1[i][9]) +  '    ' + str(grid2[i][0]) + str(grid2[i][1]) + str(grid2[i][2]) + str(grid2[i][3]) + str(grid2[i][4])+ str(grid2[i][5])+ str(grid2[i][6])+ str(grid2[i][7])+ str(grid2[i][8])+ str(grid2[i][9]))

# print_grids(tiles[0][1], tiles[1][1])

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
    # print_grids(tile_grid, transformed_grid)
    return transformed_grid

tile_transform(tiles[0][1],7)

# generate all the grids and put them in a big list of lists of grids under the same heading
#for tile in tiles:
#    tile.extend([tile_transform(tile[1],1), tile_transform(tile[1],2), tile_transform(tile[1],3), tile_transform(tile[1],4), tile_transform(tile[1],5), tile_transform(tile[1],6),tile_transform(tile[1],7)])

# do the thing Paul said where you do a backtracking search
def compare_edges(grid1,grid2,direction): # direction: right, down
    if direction == 'right':
        if all(grid1[i][-1] == grid2[i][0] for i in range(len(grid1))):
            print('It is match!')
            return True
        else:
            print('No match :(')
            return False
    if direction == 'down':
        if all(grid1[-1][i] == grid2[0][i] for i in range(len(grid1[-1]))):
            print('It is match!')
            return True
        else:
            print('No match :(')
            return False

#backtrackyman
# put in the first one
# try all the second ones with it until you get a match
# if nothing matches, go back a step

# all_tiles = [(i,j) for i in range(len(tiles)) for j in range(8)]

def backtrackyman(tiles):
    current_tile = 0
    current_tile_orientation = -1
    grid = []
    grid_orientations = []
    while len(grid) < len(tiles):
        if current_tile_orientation < 7:
            current_tile_orientation += 1
        else:
            current_tile_orientation = 0
            current_tile += 1
        while current_tile in grid:
            current_tile += 1
        if current_tile == len(tiles):
            current_tile = grid.pop()
            current_tile_orientation = grid_orientations.pop()
        else:
            print(str(current_tile) + ' ' + str(current_tile_orientation))
            if len(grid) == 0:
                grid.append(current_tile)
                grid_orientations.append(current_tile_orientation)
                current_tile = 0
                current_tile_orientation = -1
            elif 1 <= len(grid) < 12:
                if compare_edges(tile_transform(tiles[grid[-1]][1],grid_orientations[-1]), tile_transform(tiles[current_tile][1],current_tile_orientation),'right'):
                    grid.append(current_tile)
                    grid_orientations.append(current_tile_orientation)
                    current_tile = 0
                    current_tile_orientation = -1
            elif len(grid) % 12 == 0:
                if compare_edges(tile_transform(tiles[grid[-12]][1],grid_orientations[-12]), tile_transform(tiles[current_tile][1],current_tile_orientation),'down'):
                    grid.append(current_tile)
                    grid_orientations.append(current_tile_orientation)
                    current_tile = 0
                    current_tile_orientation = -1
            else:
                if compare_edges(tile_transform(tiles[grid[-1]][1], grid_orientations[-1]), tile_transform(tiles[current_tile][1], current_tile_orientation), 'right') and compare_edges(tile_transform(tiles[grid[-12]][1], grid_orientations[-12]),tile_transform(tiles[current_tile][1], current_tile_orientation), 'down'):
                    grid.append(current_tile)
                    grid_orientations.append(current_tile_orientation)
                    current_tile = 0
                    current_tile_orientation = -1
            print(grid)
    return [grid, grid_orientations]

full_grid = backtrackyman(tiles)

for i in range(12):
    print(full_grid[1][12*i:(12*i)+12])

v_trimmed_tiles = [[tile[0], tile[1][1:-1]] for tile in tiles]
trimmed_tiles = []
for tile in v_trimmed_tiles:
    trimmed_tiles.append([tile[0], [row[1:-1] for row in tile[1]]])

final_image = []
for i in range(len(full_grid[0])):
    final_image.append(tile_transform(trimmed_tiles[full_grid[0][i]][1],int(full_grid[1][i])))


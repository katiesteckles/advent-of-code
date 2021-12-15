import copy
import itertools
from collections import defaultdict

with open("2021/day15_input.txt", "r") as file:
    input = file.readlines()
    input = [list(map(int,line.strip())) for line in input]

with open("2021/day15_test.txt", "r") as file:
    testinput = file.readlines()
    testinput = [list(map(int,line.strip())) for line in testinput]

def find_diagonals(grid):
    no_of_diagonals = 2*(len(grid[0]))-1
    #print(no_of_diagonals)
    diagonals = []
    for i in range(int((no_of_diagonals-1)/2)):
        current_diag = []
        #print('Diagonal ' + str(i))
        for j in range(i+1):
            #print(grid[i-j][j])
            current_diag.append(grid[i-j][j])
        diagonals.append(current_diag)
    for i in range(int((no_of_diagonals-1)/2), no_of_diagonals):
        current_diag = []
        #print('Diagonal ' + str(i))
        for j in range(no_of_diagonals - i):
            #print(grid[int((no_of_diagonals-1)/2)-j][i - int((no_of_diagonals-1)/2)+j])
            current_diag.append(grid[int((no_of_diagonals-1)/2)-j][i - int((no_of_diagonals-1)/2)+j])
        diagonals.append(current_diag)
    return diagonals

def diags_to_grid(diagonals):
    grid = [[] for i in range((int((len(diagonals)+1)/2)))]
    for d in range(int((len(diagonals)+1)/2)):
        #print(diagonals[d])
        for i in range(len(diagonals[d])):
            grid[len(diagonals[d])-i-1].append(diagonals[d][i])
        #print(grid)
    for d in range((int((len(diagonals)+1)/2)), len(diagonals)):
        #print(diagonals[d])
        for i in range(len(diagonals[d])):
            grid[(int((len(diagonals)+1)/2))-i-1].append(diagonals[d][i])
        #print(grid)
    return grid

def find_shortest_paths(grid):
    diagonals = find_diagonals(grid)
    half = int((len(diagonals)-1)/2)
    for d in range(2, half+1):
        diagonals[d][0] += diagonals[d-1][0]
        diagonals[d][-1] += diagonals[d-1][-1]
        for e in range(1,len(diagonals[d])-1):
            diagonals[d][e] += min(diagonals[d-1][e-1],diagonals[d-1][e])
    for d in range(half+1, len(diagonals)):
        for e in range(len(diagonals[d])):
            diagonals[d][e] += min(diagonals[d-1][e],diagonals[d-1][e+1])
    return diagonals

def optimise_shortest_paths(grid,input):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            for directions in [[-1,0],[0,1],[0,-1],[1,0]]:
                if 0 <= y+directions[1] < len(grid):
                    if 0 <= x+directions[0] < len(grid[0]):
                        grid[y][x] = min(grid[y+directions[1]][x+directions[0]] + input[y][x], grid[y][x])
    return grid

# testdiags = find_diagonals(testinput)
# re_test = diags_to_grid(testdiags)
# test_paths_found = diags_to_grid(find_shortest_paths(testinput))
# optigrid = optimise_shortest_paths(diags_to_grid(find_shortest_paths(testinput)),testinput)


def iterate_grid(grid, input):
    gridsum = sum([sum(row) for row in grid])
    while True:
        print('Current optimal path: '+ str(grid[-1][-1])+ ' (sum: '+str(gridsum)+')')
        grid = optimise_shortest_paths(grid, input)
        optisum = sum([sum(row) for row in grid])
        if optisum == gridsum:
            break
        else:
            gridsum = optisum
    return grid

test_shortest_paths = diags_to_grid(find_shortest_paths(testinput))
iterate_grid(test_shortest_paths, testinput)

shortest_paths = diags_to_grid(find_shortest_paths(input))
iterate_grid(shortest_paths, input)

# part 2

# Paul's function for making the big grid

big_input=[]
for r in range(500):
    row=[]
    for c in range(500):
        new_risk = (input[r % 100][c % 100] + r//100 + c//100) % 9
        row.append(9 if new_risk==0 else new_risk )
    big_input.append(row)


shortest_big_paths = diags_to_grid(find_shortest_paths(big_input))
iterate_grid(shortest_big_paths, big_input)

print(shortest_big_paths[-1][-1])
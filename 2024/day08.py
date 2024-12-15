with open("2024/day08.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

import itertools
from collections import Counter
import pprint
import copy

test_input = ['............','........0...','.....0......','.......0....','....0.......','......A.....','............','............','........A...','.........A..','............','............']

def read_in_points(input):
    # make a list of the symbols and set up a dictionary with them and blank lists
    letters = []
    for i in range(len(input)):
        letters.extend([x for x in list(input[i]) if x != '.'])
    letters = list(set(letters))
    locs = {key: [] for key in letters}
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] in letters:
                locs[input[y][x]].append([x,y])
    return locs

def find_ends(point1,point2): # two lists of coordinates
    #print('Analysing pair at '+ str(point1) + ' and ' + str(point2))
    x_diff = point1[0] - point2[0]
    y_diff = point1[1] - point2[1]
    end_1 = [point1[0] + x_diff, point1[1] + y_diff]
    end_2 = [point2[0] - x_diff, point2[1] - y_diff]
    #print('Creating antinodes at ' + str(end_1) + ' and ' + str(end_2))
    return([end_1, end_2])

def grid_printer(input,antinodes):
    prinput = copy.deepcopy(input)
    for an in antinodes:
        if prinput[an[1]][an[0]] == '.' or prinput[an[1]][an[0]] == '#':
            prinput[an[1]] = prinput[an[1]][:an[0]] + '#' + prinput[an[1]][an[0]+1:]
        else:
            prinput[an[1]] = prinput[an[1]][:an[0]] + '%' + prinput[an[1]][an[0] + 1:]
    pprint.pp(prinput)

locations = read_in_points(input)

antinodes = []
for key in locations:
    #print(key)
    points = locations[key]
    pairs = itertools.combinations(points, 2)
    for pair in pairs:
        antinodes.extend(find_ends(pair[0],pair[1]))

antinodes_on_grid = [x for x in antinodes if 0 <= x[0] < len(input[0]) and 0 <= x[1] < len(input)]
print(len(Counter([tuple(i) for i in antinodes_on_grid])))
# grid_printer(input, antinodes_on_grid)

# Part Deux

def find_lines(point1,point2, height, width): # two pairs of coordinates plus the grid size
    #print('Analysing pair at '+ str(point1) + ' and ' + str(point2))
    x_diff = point1[0] - point2[0]
    y_diff = point1[1] - point2[1]
    # going off one way
    ends = [point1, point2, [point1[0] + x_diff, point1[1] + y_diff]]
    furthest = ends[-1]
    while furthest[0] >= 0 and furthest[0] < width and furthest[1] >= 0 and furthest[1] < height:
        ends.append([ends[-1][0] + x_diff, ends[-1][1] + y_diff])
        furthest = ends[-1]
    # going off the other way
    ends.append([point2[0] - x_diff, point2[1] - y_diff])
    furthest = ends[-1]
    while furthest[0] >= 0 and furthest[0] < width and furthest[1] >= 0 and furthest[1] < height:
        ends.append([ends[-1][0] - x_diff, ends[-1][1] - y_diff])
        furthest = ends[-1]
    # print(str(len(ends)) + ' antinodules found')
    return(ends)

antinodules = []
for key in locations:
    #print(key)
    points = locations[key]
    pairs = itertools.combinations(points, 2)
    for pair in pairs:
        antinodules.extend(find_lines(pair[0],pair[1], len(input), len(input[0])))

antinodules_on_grid = [x for x in antinodules if 0 <= x[0] < len(input[0]) and 0 <= x[1] < len(input)]
print(len(Counter([tuple(i) for i in antinodules_on_grid])))
#grid_printer(input, antinodules_on_grid)
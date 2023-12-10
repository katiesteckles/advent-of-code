with open("2023/day10_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

input_split = []
for line in input:
    input_split.append([*line])

letter_directions = {
    '|': [[0, -1], [0, 1]],
    'L': [[0, -1], [1, 0]],
    'F': [[1, 0], [0, 1]],
    'J': [[0, -1], [-1, 0]],
    '7': [[0, 1], [-1, 0]],
    '-': [[1, 0], [-1, 0]]
}


def fuck_around_and_find_outs(x,y, input):
    to_check = letter_directions[input[y][x]]
    outs = [[x+to_check[0][0], y+to_check[0][1]], [x+to_check[1][0], y+to_check[1][1]]]
    return outs


def follow_the_line(x, y, prev_x, prev_y, input):
    routes = fuck_around_and_find_outs(x,y,input)
    i = routes.index([prev_x, prev_y])
    return routes[1 - i]

start_point = [62, 90] # by observation
input_split[90][62] = 'L' # also by observation

def route_find(start_point):
    initial_directions = fuck_around_and_find_outs(start_point[0], start_point[1], input_split)
    route_list_0 = [start_point, initial_directions[0]]
    route_list_1 = [start_point, initial_directions[1]]
    while route_list_0[-1] != route_list_1[-1]:
        route_list_0.append(follow_the_line(route_list_0[-1][0], route_list_0[-1][1], route_list_0[-2][0], route_list_0[-2][1], input_split))
        # print('Route 0: '+str(route_list_0[-1]))
        route_list_1.append(follow_the_line(route_list_1[-1][0], route_list_1[-1][1], route_list_1[-2][0], route_list_1[-2][1], input_split))
        # print('Route 1: '+str(route_list_1[-1]))
    return [route_list_0, route_list_1]

routes_found = route_find(start_point)
print(len(routes_found[0])-1)

# Part 2

# some initial visualisation
import copy

def as_string(seq_of_rows):
    return '\n'.join(''.join(str(i).center(1) for i in row) for row in seq_of_rows)

grid_destroy = copy.deepcopy(input_split)

for y in range(len(grid_destroy)):
    for x in range(len(grid_destroy[y])):
        if [x,y] not in routes_found[0] and [x,y] not in routes_found[1]:
            grid_destroy[y][x] = '*'

# print(as_string(grid_destroy))

import itertools

whole_route = routes_found[0] + routes_found[1][-2:0:-1]
whole_route_backwards = routes_found[1] + routes_found[0][-2:0:-1]

lefty_dict = {
    (0, -1): [-1, 0],
    (0, 1): [1, 0],
    (1, 0): [0, -1],
    (-1, 0): [0, 1]
}

righty_dict = {
    (0, -1): [1, 0],
    (0, 1): [-1, 0],
    (1, 0): [0, 1],
    (-1, 0): [0, -1]
}

def everything_you_owns_in_a_box_to_the_dict(route_list, dict):
    lefts = set()
    for i in range(len(route_list)-1):
        change = (route_list[i+1][0] - route_list[i][0], route_list[i+1][1] - route_list[i][1])
        new_left = (route_list[i+1][0] + dict[change][0], route_list[i+1][1] + dict[change][1])
        if [new_left[0], new_left[1]] not in route_list:
            lefts.add(new_left)
    print(lefts)
    return lefts

grid_both_paths = copy.deepcopy(input_split)

for_rights = everything_you_owns_in_a_box_to_the_dict(whole_route, righty_dict)
back_lefts = everything_you_owns_in_a_box_to_the_dict(whole_route_backwards, lefty_dict)
insiders = for_rights.union(back_lefts)
for y in range(len(grid_both_paths)):
    for x in range(len(grid_both_paths[y])):
        if [x,y] not in whole_route:
            if (x,y) in insiders:
                grid_both_paths[y][x] = '#'
            else:
                grid_both_paths[y][x] = '*'


# print(as_string(grid_both_paths))

def flood_fill(insiders, whole_route):
    all_insiders = insiders
    new_insiders = {'temp'}
    while len(new_insiders) > 0:
        new_insiders = set()
        for insider in all_insiders:
            adjacents = [(insider[0]+1, insider[1]), (insider[0], insider[1]+1), (insider[0]-1, insider[1]), (insider[0], insider[1]-1)]
            for cell in adjacents:
                if cell not in all_insiders and [cell[0], cell[1]] not in whole_route:
                    new_insiders.add(cell)
            all_insiders = all_insiders.union(new_insiders)
    return all_insiders

# testy bit

test_insiders = flood_fill({(63, 63)}, whole_route) # found one of the hash cells on the boundary of the big lake
tester_pot = copy.deepcopy(input_split)
for y in range(len(tester_pot)):
    for x in range(len(tester_pot[y])):
        if (x,y)  in test_insiders:
            tester_pot[y][x] = '#'
        else:
            tester_pot[y][x] = '*'
# print(as_string(tester_pot))

all_insiders = flood_fill(insiders, whole_route)
print(len(all_insiders))

Test

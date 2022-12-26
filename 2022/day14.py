with open("2022/day14_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

coordinates_list = [line.split(' -> ') for line in input]
coordinate_pairs = [[[int(item[0]),int(item[1])] for item in [pair.split(',') for pair in line]] for line in coordinates_list]

test = ['498,4 -> 498,6 -> 496,6','503,4 -> 502,4 -> 502,9 -> 494,9']
coordinates_list_test = [line.split(' -> ') for line in test]
coordinate_pairs_test = [[[int(item[0]),int(item[1])] for item in [pair.split(',') for pair in line]] for line in coordinates_list_test]

floor_height = max([max(y_coord) for y_coord in [[pair[1] for pair in line] for line in coordinate_pairs]]) + 2
test_floor_height = max([max(y_coord) for y_coord in [[pair[1] for pair in line] for line in coordinate_pairs_test]]) + 2

def read_in_line(dict, line):
    for vertex in range(len(line)-1):
        print(vertex, vertex+1)
        if line[vertex+1][0] - line[vertex][0] >= 0: x_sign = 1
        else: x_sign = -1
        if line[vertex+1][1] - line[vertex][1] >= 0: y_sign = 1
        else: y_sign = -1
        print(line[vertex][0], line[vertex + 1][0], x_sign)
        print(line[vertex][1], line[vertex + 1][1], x_sign)
        for x in range(line[vertex][0], line[vertex + 1][0]+x_sign, x_sign):
            for y in range(line[vertex][1],line[vertex + 1][1]+y_sign, y_sign):
                print(x,y)
                coords = tuple([x,y])
                dict[coords] = '#'
    return dict

test_dict = {}
for line in coordinate_pairs_test:
    test_dict = read_in_line(test_dict, line)

big_dict_energy = {}
for line in coordinate_pairs:
    big_dict_energy = read_in_line(big_dict_energy,line)

initial_point = (500,0)

def drop_a_bit_of_sand(dict, floor_height):
    sand_not_moving = 0
    current_sand_location = initial_point
    while sand_not_moving == 0:
        # if nozzle is clogged
        if dict.get((current_sand_location[0],current_sand_location[1])) == 'o':
            sand_not_moving = 1
        # if the space below the current location is empty
        elif dict.get((current_sand_location[0], current_sand_location[1]+1), 'No') == 'No':
        # move the sand down
            current_sand_location = (current_sand_location[0], current_sand_location[1]+1)
        # if it isn't, check down and left and move it there
        elif dict.get((current_sand_location[0]-1, current_sand_location[1]+1), 'No') == 'No':
            current_sand_location = (current_sand_location[0]-1,current_sand_location[1] + 1)
        # if it isn't, check down and right and move it there
        elif dict.get((current_sand_location[0]+1, current_sand_location[1]+1), 'No') == 'No':
            current_sand_location = (current_sand_location[0]+1,current_sand_location[1] + 1)
        # otherwise it stops
        else:
            dict[current_sand_location] = 'o'
            sand_not_moving = 1
    #visualise_sand(dict)
    return dict


def visualise_sand(dict):
    grid = []
    x_min = min([x_coord for x_coord in [entry[0] for entry in dict]])
    x_max = max([x_coord for x_coord in [entry[0] for entry in dict]])
    y_min = min([y_coord for y_coord in [entry[1] for entry in dict]])
    y_max = max([y_coord for y_coord in [entry[1] for entry in dict]])
    print(x_min,x_max,y_min,y_max)
    for y in range(y_min,y_max+1):
        grid.append([])
        for x in range(x_min,x_max+1):
            grid[y-y_min].append(' ')
    for key in dict:
        grid[key[1]-y_min][key[0]-x_min] = dict[key]
    for gl in grid:
        print(''.join(gl))
    return grid


#sands_dropped = 0
#while True:
#    drop_a_bit_of_sand(test_dict, test_floor_height)
#    sands_dropped +=1
#    print(sands_dropped)

# the answer is one more than this apparently

# Part B


test_triangle_height = test_floor_height - initial_point[1]
read_in_line(test_dict, [[int(490-(test_triangle_height/2)), test_floor_height],[int(510+(test_triangle_height/2)),test_floor_height]])

triangle_height = floor_height - initial_point[1]
read_in_line(big_dict_energy, [[int(400-(triangle_height/2)), floor_height],[int(600+(triangle_height/2)),floor_height]])


sands_dropped = 0
while (500,0) not in big_dict_energy:
    drop_a_bit_of_sand(big_dict_energy, floor_height)
    sands_dropped +=1
    print(sands_dropped)

visualise_sand(big_dict_energy)
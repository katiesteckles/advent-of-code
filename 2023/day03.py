with open("2023/day03_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

test_grid = ['abcdef','ghijkl','mnopqr','stuvwx']
digits = "0123456789"


# abcdef
# ghijkl
# mnopqr
# stuvwx

def get_part_neighbours(x,y,digs,input):  # first the column then the row of the left hand cell, 0-indexed
    neighbours = []
    nottop = False
    notbot = False
    notleft = False
    if y - 1 >= 0: nottop = True
    if y + 1 < len(input): notbot = True
    if x - 1 >= 0: notleft = True
    neighbours.append(input[y - 1][x]) if nottop else neighbours.append('') # above the start cell
    neighbours.append(input[y - 1][x - 1]) if (nottop and notleft) else neighbours.append('') # top left corner
    neighbours.append(input[y][x - 1]) if notleft else neighbours.append('') # left of start cell
    neighbours.append(input[y + 1][x - 1]) if notleft and notbot else neighbours.append('') # bottom left corner
    neighbours.append(input[y + 1][x]) if notbot else neighbours.append('')# below the start cell
    if digs == 1:
        if x + 1 < len(input[y]):
            neighbours.append(input[y + 1][x + 1]) if notbot else neighbours.append('')
            neighbours.append(input[y][x + 1])
            neighbours.append(input[y - 1][x + 1]) if nottop else neighbours.append('')
        else:
            neighbours.extend(['','',''])
    if digs == 2:
        if x + 1 < len(input[y]):
            neighbours.append(input[y + 1][x + 1]) if notbot else neighbours.append('')
        if x + 2 < len(input[y]):
            neighbours.append(input[y + 1][x + 2]) if notbot else neighbours.append('')
            neighbours.append(input[y][x + 2])
            neighbours.append(input[y - 1][x + 2]) if nottop else neighbours.append('')
        if x + 1 < len(input[y]):
            neighbours.append(input[y - 1][x + 1]) if nottop else neighbours.append('')
    if digs == 3:
        if x + 1 < len(input[y]):
            neighbours.append(input[y + 1][x + 1]) if notbot else neighbours.append('')
        if x + 2 < len(input[y]):
            neighbours.append(input[y + 1][x + 2]) if notbot else neighbours.append('')
        if x + 3 < len(input[y]):
            neighbours.append(input[y + 1][x + 3]) if notbot else neighbours.append('')
            neighbours.append(input[y][x + 3])
            neighbours.append(input[y - 1][x + 3]) if nottop else neighbours.append('')
        if x + 2 < len(input[y]):
            neighbours.append(input[y - 1][x + 2]) if nottop else neighbours.append('')
        if x + 1 < len(input[y]):
            neighbours.append(input[y - 1][x + 1]) if nottop else neighbours.append('')
    return neighbours


get_part_neighbours(1,3,2,test_grid)

test_input = ['467..114..','...*......','..35..633.','......#...','617*......','.....+.58.','..592.....','......755.',
              '...$.*....','.664.598..']


def find_partnos(input):
    part_nos = []
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] in digits and (x == 0 or (input[y][x - 1] not in digits)):  # if it's the start of a number
                # find the other end
                digs = 0
                while x + digs < len(input[y]) and input[y][x + digs] in digits:
                    digs += 1
                print('Part number found at position (' + str(x) + ', ' + str(y) + ') with length ' + str(
                    digs) + ' and value ' + input[y][x:x + digs])
                part_nos.append([x,y,digs,int(input[y][x:x + digs])])
    return part_nos


test_parts = find_partnos(test_input)
partsparts = find_partnos(input)

total = 0
for part in partsparts:
    included = 1
    neighbours = get_part_neighbours(part[0],part[1],part[2],input)
    print(part[3],neighbours)
    for neighbour in neighbours:
        if (neighbour not in digits) and (neighbour != '.'):
            total += part[3] * included
            included = 0


# Part 2

def find_parts_with_gears(parts,input):
    gear_parts = []
    for part in parts:
        neighbours = get_part_neighbours(part[0],part[1],part[2],input)
        if '*' in neighbours:
            gear_parts.append([part[0],part[1],part[2],part[3],neighbours.index('*')])
    return gear_parts

find_parts_with_gears(test_parts, test_input)
find_parts_with_gears(partsparts, input)

adjacency_dict = {
    (1, 0): [0, -1],
    (1, 1): [-1, -1],
    (1, 2): [-1, 0],
    (1, 3): [-1, 1],
    (1, 4): [0, 1],
    (1, 5): [1, 1],
    (1, 6): [1, 0],
    (1, 7): [1, -1],
    (2, 0): [0, -1],
    (2, 1): [-1, -1],
    (2, 2): [-1, 0],
    (2, 3): [-1, 1],
    (2, 4): [0, 1],
    (2, 5): [1, 1],
    (2, 6): [2, 1],
    (2, 7): [2, 0],
    (2, 8): [2, -1],
    (2, 9): [1, -1],
    (3, 0): [0, -1],
    (3, 1): [-1, -1],
    (3, 2): [-1, 0],
    (3, 3): [-1, 1],
    (3, 4): [0, 1],
    (3, 5): [1, 1],
    (3, 6): [2, 1],
    (3, 7): [3, 1],
    (3, 8): [3, 0],
    (3, 9): [3, -1],
    (3, 10): [2, -1],
    (3, 11): [1, -1]
}

def find_gears(input):
    gears = {} # have a dictionary of gears where the keys are tuples of gear coordinates
    gearparts = find_parts_with_gears(find_partnos(input), input)
    # look at list of parts that are next to gears
    for gearpart in gearparts: # for each one locate the gear [x, y, digs, part_no, pos]
        gear_coords = (gearpart[0] + adjacency_dict[(gearpart[2],gearpart[4])][0], gearpart[1] + adjacency_dict[(gearpart[2],gearpart[4])][1])
        print('Gear located at '+str(gear_coords)+' adjacent to part number '+str(gearpart[3]))
        if gear_coords in gears: # if there's already a key then append it, otherwise create the key
            gears[gear_coords].append(gearpart[3])
        else:
            gears[gear_coords] = [gearpart[3]]
    return gears

gears = find_gears(input)

max([len(thing) for thing in gears.values()]) # hope it's 2

total_ratios = 0
for pair in gears.values():
    if len(pair) == 2:
        total_ratios += (pair[0] * pair[1])

print(total_ratios)
import copy
with open("2021/day05_input.txt", "r") as file:
    input = file.readlines()

list_of_lines = [[list(map(int,point.split(','))) for point in line[:-1].split(' -> ')] for line in input]

def find_horzverts(lines):
    horzverts = []
    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            print(str(line))
            horzverts.append(line)
    return horzverts

horzverts = find_horzverts(list_of_lines)

def read_line(line):
    direction = [0,0] # horiztonal, vertical (1,0,-1)
    for i in range(2):
        if line[0][i] > line[1][i]:
            direction[i] = -1
        elif line[0][i] == line[1][i]:
            direction[i] = 0
        elif line[0][i] < line[1][i]:
            direction[i] = 1
    length = max(abs(line[0][i]-line[1][i]) for i in range(2))
    newvents = []
    newvents.append(line[0])
    for i in range(length):
        new_vent = [x + y for x, y in zip(newvents[-1], direction)]
        newvents.append(new_vent)
    return newvents

def encode_vent(vent):
    return((1000*vent[0]) + vent[1])

def decode_vent(vent):
    return([int(vent/1000),vent-(1000*int(vent/1000))])

def dict_a_line(line,dict):
    for point in read_line(line):
        if encode_vent(point) in dict:
            dict[encode_vent(point)] += 1
        else:
            dict[encode_vent(point)] = 1

vents = {}
for line in horzverts:
    dict_a_line(line,vents)

danger_spots = [decode_vent(x) for x in vents if vents[x]>1]

# part 2

vents2 = {}
for line in list_of_lines:
    dict_a_line(line,vents2)

danger_spots2 = [decode_vent(x) for x in vents2 if vents2[x]>1]

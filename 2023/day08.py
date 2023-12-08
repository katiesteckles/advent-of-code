with open("2023/day08_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

directions = input[0]
input = input[2:]

network_dict = {}
for line in input:
    bits = line.split(' = ')
    network_dict[bits[0]] = bits[1][1:-1].split(', ')

current_location = 'AAA'
steps_taken = 0
while current_location != 'ZZZ':
    for i in range(len(directions)):
        print(current_location)
        if directions[i] == 'L':
            current_location = network_dict[current_location][0]
        elif directions[i] == 'R':
            current_location = network_dict[current_location][1]
        steps_taken += 1

print(steps_taken)

# Part 2

start_points = [place for place in network_dict.keys() if place[-1] == 'A']

import copy

steps_per_point = []
for point in start_points:
    current_location = copy.deepcopy(point)
    steps_taken = 0
    while current_location[-1] != 'Z':
        for i in range(len(directions)):
            print(current_location)
            if directions[i] == 'L':
                current_location = network_dict[current_location][0]
            elif directions[i] == 'R':
                current_location = network_dict[current_location][1]
            steps_taken += 1
    steps_per_point.append(steps_taken)

import math as maths

print(maths.lcm(*steps_per_point))

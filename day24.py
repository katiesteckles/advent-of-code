import copy
import re

with open("day24_input.txt", "r") as file:
    moves = file.readlines()
moves = [move[:-1] for move in moves]

def parse_line(line):
    i = 0
    line_commands = []
    while i < len(line):
        if line[i] == 'n':
            if line[i+1] == 'e':
                line_commands.append((0.5,-1))
                i += 2
            elif line[i+1] == 'w':
                line_commands.append((-0.5,-1))
                i += 2
        elif line[i] == 's':
            if line[i+1] == 'e':
                line_commands.append((0.5,1))
                i += 2
            elif line[i+1] == 'w':
                line_commands.append((-0.5,1))
                i += 2
        elif line[i] == 'e':
            line_commands.append((1, 0))
            i += 1
        elif line[i] == 'w':
            line_commands.append((-1, 0))
            i += 1
    return line_commands

parse_line(moves[0])

cells_dict = {}

for line in moves:
    position = (0,0)
    line_moves = parse_line(line)
    print('Executing moves: ' + str(line_moves))
    for move in line_moves:
        position = (position[0] + move[0], position[1] + move[1])
    print('Checking cell in position ' + str(position))
    if position in cells_dict and cells_dict[position] == 'B':
        print('Cell is currently B; changing to W')
        cells_dict[position] = 'W'
    elif position not in cells_dict or cells_dict[position] == 'W':
        print('Cell is currently W; changing to B')
        cells_dict[position] = 'B'

sum(x =='B' for x in cells_dict.values())
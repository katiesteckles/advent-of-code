with open("2024/day06.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

# input[y][x] = (x,y) in grid (0-indexed); left/right = -/+ x, up/down = -/+ y

def find_him(input):
    for i in range(len(input)):
        if '^' in input[i]:
            igp = [input[i].find('^'), i]
        if '>' in input[i]:
            igp = [input[i].find('>'), i]
        if 'v' in input[i]:
            igp = [input[i].find('v'), i]
        if '<' in input[i]:
            igp = [input[i].find('<'), i]
    return igp

def move_guard(input):
    [x, y] = find_him(input)
    if input[y][x] == '^':
        # guard goes up
        if y-1 < 0:
            return input, False
        else:
            if input[y-1][x] != '#':  # nothing there, can move
                input[y-1] = input[y-1][:x]+'^'+input[y-1][x+1:]
                input[y] = input[y][:x] + 'X' + input[y][x+1:]
                return input, True
            else:  # turn, turn, turn (right 90)
                input[y] = input[y][:x] + '>' + input[y][x+1:]
                return input, True
    if x+1 >= len(input[y]):
        return input, False
    else:
        if input[y][x] == '>':
            # guard goes right
            if input[y][x+1] != '#':  # nothing there, can move
                input[y] = input[y][:x+1] + '>' + input[y][x+2:]
                input[y] = input[y][:x] + 'X' + input[y][x+1:]
                return input, True
            else:  # turn, turn, turn (right 90)
                input[y] = input[y][:x] + 'v' + input[y][x+1:]
                return input, True
    if input[y][x] == 'v':
        # guard goes down
        if y+1 >= len(input):
            return input, False
        else:
            if input[y+1][x] != '#':  # nothing there, can move
                input[y+1] = input[y+1][:x]+'v'+input[y+1][x+1:]
                input[y] = input[y][:x] + 'X' + input[y][x+1:]
                return input, True
            else: # turn, turn, turn (right 90)
                input[y] = input[y][:x] + '<' + input[y][x+1:]
                return input, True
    if input[y][x] == '<':
        # guard goes left
        if x-1 < 0:
            return input, False
        else:
            if input[y][x-1] != '#': # nothing there, can move
                input[y] = input[y][:x-1] + '<' + input[y][x:]
                input[y] = input[y][:x] + 'X' + input[y][x+1:]
                return input, True
            else: # turn, turn, turn (right 90)
                input[y] = input[y][:x] + '^' + input[y][x+1:]
                return input, True

import copy
import pprint
maze = copy.deepcopy(input)

stillgoing = True
while stillgoing == True:
    maze, stillgoing = move_guard(maze)
#pprint.pp(maze)

totalpos = 1
for i in range(len(maze)):
    totalpos += maze[i].count('X')

print(totalpos)

# Part B

# haha this takes about half an hour to run

placeshesbeen = []
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == 'X' or maze[y][x] == 'v' :
            placeshesbeen.append([x,y])

testinput = ['....#.....', '.........#', '..........', '..#.......', '.......#..', '..........', '.#..^.....', '........#.', '#.........', '......#...']

start_pos = find_him(input)

def loggy_move_guard(input, log, loops):
    [x, y] = find_him(input)
    if [x, y, input[y][x]] in log[:-1]:
        loops += 1
        # print('Found '+str(loops)+ ' loops')
        return input, False, log, loops
    if input[y][x] == '^':
        # guard goes up
        if y-1 < 0:
            return input, False, log, loops
        else:
            if input[y-1][x] != '#':  # nothing there, can move
                input[y-1] = input[y-1][:x]+'^'+input[y-1][x+1:]
                input[y] = input[y][:x] + '.' + input[y][x+1:]
                log.append([x, y-1, '^'])
                return input, True, log, loops
            else:  # turn, turn, turn (right 90)
                input[y] = input[y][:x] + '>' + input[y][x+1:]
                log.append([x, y, '>'])
                return input, True, log, loops
    if x+1 >= len(input[y]):
        return input, False, log, loops
    else:
        if input[y][x] == '>':
            # guard goes right
            if input[y][x+1] != '#':  # nothing there, can move
                input[y] = input[y][:x+1] + '>' + input[y][x+2:]
                input[y] = input[y][:x] + '.' + input[y][x+1:]
                log.append([x+1, y, '>'])
                return input, True, log, loops
            else:  # turn, turn, turn (right 90)
                input[y] = input[y][:x] + 'v' + input[y][x+1:]
                log.append([x, y, 'v'])
                return input, True, log, loops
    if input[y][x] == 'v':
        # guard goes down
        if y+1 >= len(input):
            return input, False, log, loops
        else:
            if input[y+1][x] != '#':  # nothing there, can move
                input[y+1] = input[y+1][:x]+'v'+input[y+1][x+1:]
                input[y] = input[y][:x] + '.' + input[y][x+1:]
                log.append([x, y+1, 'v'])
                return input, True, log, loops
            else: # turn, turn, turn (right 90)
                input[y] = input[y][:x] + '<' + input[y][x+1:]
                log.append([x, y, '<'])
                return input, True, log, loops
    if input[y][x] == '<':
        # guard goes left
        if x-1 < 0:
            return input, False, log, loops
        else:
            if input[y][x-1] != '#': # nothing there, can move
                input[y] = input[y][:x-1] + '<' + input[y][x:]
                input[y] = input[y][:x] + '.' + input[y][x+1:]
                log.append([x-1, y, '<'])
                return input, True, log, loops
            else: # turn, turn, turn (right 90)
                input[y] = input[y][:x] + '^' + input[y][x+1:]
                log.append([x, y, '^'])
                return input, True, log, loops

loops = 0
mod_maze = copy.deepcopy(input)
for xypair in placeshesbeen:
    x, y = xypair
    wihn = find_him(mod_maze) # where is he now
    mod_maze[wihn[1]] = mod_maze[wihn[1]][:wihn[0]] + '.' + mod_maze[wihn[1]][wihn[0]+1:]  # rub him out
    mod_maze[start_pos[1]] = mod_maze[start_pos[1]][:start_pos[0]] + '^' + mod_maze[start_pos[1]][start_pos[0] + 1:]  # pop him back at the start
    # pprint.pp(mod_maze)
    if mod_maze[y][x] not in {'<','>','v','^'}:
        mod_maze[y] = mod_maze[y][:x] + '#' + mod_maze[y][x+1:] # put in that one barrel
        # print('Trying a barrel at '+str(x)+', '+str(y)+'...')
        log = []
        stillgoing = True
        while stillgoing == True:
            mod_maze, stillgoing, log, loops = loggy_move_guard(mod_maze, log, loops)
        mod_maze[y] = mod_maze[y][:x] + '.' + mod_maze[y][x + 1:]  # take out that one barrel

print(loops)
#254 loops for values of y up to and including 38
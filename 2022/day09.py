with open("2022/day09_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]
    input = [line.split(' ') for line in input]

import copy

test_input = [['R','4'],['U','4'],['L','3'],['D','1'],['R','4'],['D','1'],['L','5'],['R','2']]
longer_test_input= [['R','5'],['U','8'],['L','8'],['D','3'],['R','17'],['D','10'],['L','25'],['U','20']]

# head_pos and tail_pos as (x,y)


def update_tail_pos(head_pos, tail_pos, head_move):
    # print('Head pos: '+str(head_pos)+'; Tail pos: '+str(tail_pos))
    head_pos = [head_pos[0] + head_move[0], head_pos[1] + head_move[1]]
    tail_move = [0, 0]
    if head_pos[0] == tail_pos[0]:
        if head_pos[1] - tail_pos[1] > 1:
            tail_move = [0, 1]
        if head_pos[1] - tail_pos[1] < -1:
            tail_move = [0, -1]
    if head_pos[1] == tail_pos[1]:
        if head_pos[0] - tail_pos[0] > 1:
            tail_move = [1, 0]
        if head_pos[0] - tail_pos[0] < -1:
            tail_move = [-1, 0]
    # diagonal cases
    if head_pos[0] < tail_pos[0]:
        if head_pos[1] - tail_pos[1] > 1:
            tail_move = [-1, 1]
        if head_pos[1] - tail_pos[1] < -1:
            tail_move = [-1, -1]
    if head_pos[0] > tail_pos[0]:
        if head_pos[1] - tail_pos[1] > 1:
            tail_move = [1, 1]
        if head_pos[1] - tail_pos[1] < -1:
            tail_move = [1, -1]
    if head_pos[1] < tail_pos[1]:
        if head_pos[0] - tail_pos[0] > 1:
            tail_move = [1, -1]
        if head_pos[0] - tail_pos[0] < -1:
            tail_move = [-1, -1]
    if head_pos[1] > tail_pos[1]:
        if head_pos[0] - tail_pos[0] > 1:
            tail_move = [1, 1]
        if head_pos[0] - tail_pos[0] < -1:
            tail_move = [-1, 1]
    tail_pos = [tail_pos[0] + tail_move[0], tail_pos[1] + tail_move[1]]
    #print('Head pos: ' + str(head_pos) + '; tail pos: ' + str(tail_pos))
    return [head_pos, tail_pos, tail_move]


directions_dict = {
    'R': [1, 0],
    'L': [-1, 0],
    'U': [0, 1],
    'D': [0, -1]
}

head_pos = [0, 0]
tail_pos = [0, 0]

print('Head pos: ' + str(head_pos) + '; tail pos: ' + str(tail_pos))
tail_poses = [tuple(tail_pos)]
for line in input:
    head_move = directions_dict[line[0]]
    print(str(line) + '; moving ' + str(head_move) + ' for ' + str(line[1]) + ' spaces')
    for i in range(int(line[1])):
        new_poses = update_tail_pos(head_pos, tail_pos, head_move)
        head_pos = new_poses[0]
        tail_pos = new_poses[1]
        tail_poses.append(tuple(tail_pos))

visited = len(set(tail_poses))
print(visited)

# Part B

snake_pos = []
for i in range(10): snake_pos.append([0,0])

# Per move
print('Snake pos: ' + str(snake_pos))
long_tail_poses = [tuple(snake_pos[-1])]
for line in input:
    snake_moves = [directions_dict[line[0]]]
    for i in range(9): snake_moves.append([0,0])
    print(str(line) + '; moving head ' + str(snake_moves[0]) + ' for ' + str(line[1]) + ' spaces')
        for j in range(int(line[1])):
            for k in range(9):
                new_poses = update_tail_pos(snake_pos[k], snake_pos[k+1], snake_moves[k])
                snake_pos[k] = new_poses[0]
                snake_moves[k+1] = new_poses[2]
                long_tail_poses.append(tuple(snake_pos[-1]))
            snake_pos[-1] = [snake_pos[-1][0]+snake_moves[-1][0], snake_pos[-1][1]+snake_moves[-1][1]]
            long_tail_poses.append(tuple(snake_pos[-1]))
            print('Pos: '+str(snake_pos))

long_visited = len(set(long_tail_poses))
print(long_visited)

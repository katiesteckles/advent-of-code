import copy
with open("day12_input.txt", "r") as file:
    rows = file.readlines()

commands = [[row[0],int(row[1:-1])] for row in rows]
test_commands = [['F',10],['N',3], ['F',7],['R',90],['F',11]]

# directions: north = 0, northeast = 1, east = 2, southeast = 3, south = 4, southwest = 5, west = 6, northwest = 7

def parse_command(command,position):
    current_pos = copy.deepcopy(position)
    print(current_pos)
    if command[0] == 'R':
        print('Turning right ' + str(command[1]))
        current_pos[2] = int((current_pos[2] + (command[1] / 45)) % 8)
    if command[0] == 'L':
        print('Turning left ' + str(command[1]))
        current_pos[2] = int((current_pos[2] - (command[1] / 45)) % 8)
    if command[0] == 'N':
        print('Going north ' + str(command[1]))
        current_pos[1] -= command[1]
    if command[0] == 'S':
        print('Going south ' + str(command[1]))
        current_pos[1] += command[1]
    if command[0] == 'E':
        print('Going east ' + str(command[1]))
        current_pos[0] += command[1]
    if command[0] == 'W':
        print('Going west ' + str(command[1]))
        current_pos[0] -= command[1]
    if command[0] == 'F':
        print('Going forward ' + str(command[1]))
        if current_pos[2] == 0:
            current_pos[1] -= command[1]
        if current_pos[2] == 1:
            current_pos[1] -= command[1]
            current_pos[0] += command[1]
        if current_pos[2] == 2:
            current_pos[0] += command[1]
        if current_pos[2] == 3:
            current_pos[1] += command[1]
            current_pos[0] += command[1]
        if current_pos[2] == 4:
            current_pos[1] += command[1]
        if current_pos[2] == 5:
            current_pos[1] += command[1]
            current_pos[0] -= command[1]
        if current_pos[2] == 6:
            current_pos[0] -= command[1]
        if current_pos[2] == 7:
            current_pos[1] -= command[1]
            current_pos[0] -= command[1]
    return current_pos

initial_position = [0,0,2] # position = [0 = x, 1 = y, 2 = orientation]
list_of_positions = [initial_position]
for command in commands:
    new_position = parse_command(command,list_of_positions[-1])
    list_of_positions.append(new_position)
print(list_of_positions[-1])
print(abs(list_of_positions[-1][0]) + abs(list_of_positions[-1][1]))
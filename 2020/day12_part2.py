import copy
with open("day12_input.txt", "r") as file:
    rows = file.readlines()

commands = [[row[0],int(row[1:-1])] for row in rows]
test_commands = [['F',10],['N',3], ['F',7],['R',90],['F',11]]

# directions: north = 0, northeast = 1, east = 2, southeast = 3, south = 4, southwest = 5, west = 6, northwest = 7

def move_waypoint_and_boat(command,boat_position,rel_waypoint_position):
    waypoint_relpos = copy.deepcopy(rel_waypoint_position)
    boat_pos = copy.deepcopy(boat_position)
    print(boat_pos,waypoint_relpos)
    if command[0] == 'R':
        print('Rotating the waypoint right ' + str(command[1]))
        #relative_waypoint_pos = [waypoint_pos[0]-boat_pos[0], waypoint_pos[1]-boat_pos[1]]
        for i in range(int(command[1]/90)):
            waypoint_relpos = [-waypoint_relpos[1],waypoint_relpos[0]]
    if command[0] == 'L':
        print('Rotating the waypoint left ' + str(command[1]))
        for i in range(int(command[1]/90)):
            waypoint_relpos = [waypoint_relpos[1],-waypoint_relpos[0]]
    if command[0] == 'N':
        print('Moving the waypoint north ' + str(command[1]))
        waypoint_relpos[1] -= command[1]
    if command[0] == 'S':
        print('Moving the waypoint south ' + str(command[1]))
        waypoint_relpos[1] += command[1]
    if command[0] == 'E':
        print('Moving the waypoint east ' + str(command[1]))
        waypoint_relpos[0] += command[1]
    if command[0] == 'W':
        print('Moving the waypoint west ' + str(command[1]))
        waypoint_relpos[0] -= command[1]
    if command[0] == 'F':
        print('Going to the waypoint ' + str(command[1]) + ' times')
        amount_of_move_x = waypoint_relpos[0] * command[1]
        amount_of_move_y = waypoint_relpos[1] * command[1]
        #waypoint_pos = [waypoint_pos[0] + amount_of_move_x, waypoint_pos[1] + amount_of_move_y]
        boat_pos = [boat_pos[0] + amount_of_move_x, boat_pos[1] + amount_of_move_y]
    return [boat_pos, waypoint_relpos]

initial_boat_position = [0,0] # position = [0 = x, 1 = y]
initial_waypoint_position = [10,-1]
list_of_positions = [[initial_boat_position,initial_waypoint_position]]
for command in commands:
    new_positions = move_waypoint_and_boat(command,list_of_positions[-1][0], list_of_positions[-1][1])
    list_of_positions.append(new_positions)
print(list_of_positions[-1])
print(abs(list_of_positions[-1][0][0]) + abs(list_of_positions[-1][0][1]))
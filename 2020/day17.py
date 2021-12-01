import copy
with open("day17_input.txt", "r") as file:
    grid = file.readlines()

grid = [line[:-1] for line in grid]
test_grid = ['.#.','..#','###']

def in_da_hood(x,y,z):
    hood = set()
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                hood.add((x+i, y+j, z+k))
    hood.remove((x,y,z))
    return hood

    # return ([x+1, y+1, z+1],[x+1,y+1,z],[x+1,y+1,z-1],
    #         [x+1, y, z+1],[x+1,y,z],[x+1,y,z-1],
    #         [x+1, y-1, z+1],[x+1,y-1,z],[x+1,y-1,z-1],
    #         [x, y+1, z+1],[x,y+1,z],[x,y+1,z-1],
    #         [x, y, z+1],[x,y,z-1],
    #         [x, y-1, z+1],[x,y-1,z],[x,y-1,z-1],
    #         [x-1, y+1, z+1],[x-1,y+1,z],[x-1,y+1,z-1],
    #         [x-1, y, z+1],[x-1,y,z],[x-1,y,z-1],
    #         [x-1, y-1, z+1],[x-1,y-1,z],[x-1,y-1,z-1]]

active_points = set()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            active_points.add((i,j,0))


# create a function that iterates
def iterate(points):
    active_points = copy.deepcopy(points)
    points_to_check = copy.deepcopy(points) # start with the current set of active points
    for point in points:
        points_to_check |= in_da_hood(point[0],point[1],point[2])
    print('Checking ' + str(len(points_to_check)) + ' points...')
    points_to_add = set()
    points_to_remove = set()
    for check_point in points_to_check:
        da_hood = in_da_hood(check_point[0],check_point[1],check_point[2])
        if check_point in active_points:
            if len([neighbour for neighbour in da_hood if neighbour in active_points]) in range(2,4):
                print(str(check_point) + ' is stayin\' alive')
            else:
                points_to_remove.add(check_point)
                print(str(check_point) + ' has died of dysentry')
        else:
            if len([neighbour for neighbour in da_hood if neighbour in active_points]) == 3:
                points_to_add.add(check_point)
                print(str(check_point) + ' is alive... ALIVE!')
            else:
                print(str(check_point) + ' remains dead')
    active_points |= points_to_add
    active_points -= points_to_remove
    print('New list of active points: ' + str(active_points))
    return active_points

active_points1 = iterate(active_points)

active_points_list = []
active_points_list.append(copy.deepcopy(active_points))

for i in range(6):
    active_points_list.append(iterate(active_points_list[i]))


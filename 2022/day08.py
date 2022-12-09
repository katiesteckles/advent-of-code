with open("2022/day08_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

test_input = ['30373','25512','65332','33549','35390']


def tree_sightlines(grid, x, y):
    grid_height = len(grid)
    grid_width = len(grid[0])
    print('Grid is '+str(grid_width)+' wide by '+str(grid_height)+' high; current tree in position (' + str(x)+', '+str(y)+') with height '+grid[y][x])
    directions = []
    # up
    up_trees = []
    for y_val in range(y):
        up_trees.append(grid[y_val][x])
    print('Trees above: ' + str(up_trees))
    if up_trees == [] or max([int(tree) for tree in up_trees]) < int(grid[y][x]):
        directions.append(0)
    else:
        directions.append(1)
    # down
    down_trees = []
    for y_val in range(y+1, grid_height):
        down_trees.append(grid[y_val][x])
    print('Trees below: '+str(down_trees))
    if down_trees == [] or max([int(tree) for tree in down_trees]) < int(grid[y][x]):
        directions.append(0) # it's visible from this direction
    else:
        directions.append(1) # something is blocking it
    # left
    left_trees = []
    for x_val in range(x):
        left_trees.append(grid[y][x_val])
    print('Trees to the left: ' + str(left_trees))
    if left_trees == [] or max([int(tree) for tree in left_trees]) < int(grid[y][x]):
        directions.append(0)
    else:
        directions.append(1)
    # right
    right_trees = []
    for x_val in range(x+1, grid_width):
        right_trees.append(grid[y][x_val])
    print('Trees to the right: ' + str(right_trees))
    if right_trees == [] or max([int(tree) for tree in right_trees]) < int(grid[y][x]):
        directions.append(0)
    else:
        directions.append(1)
    print(sum(directions))
    return(directions)

tree_sightlines(test_input,1,1)

visible_tree_count = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        if sum(tree_sightlines(input,x,y)) < 4:
            visible_tree_count +=1

print(visible_tree_count)

# Part B

def scenic_score(grid, x, y):
    grid_height = len(grid)
    grid_width = len(grid[0])
    print('Grid is '+str(grid_width)+' wide by '+str(grid_height)+' high; current tree in position (' + str(x)+', '+str(y)+') with height '+grid[y][x])
    # up
    up_trees = ['-1']
    no_up_trees = -1
    for y_val in range(y-1, -1, -1):
        up_trees.append(grid[y_val][x])
    for tree in up_trees[1:]:
        if int(tree) >= int(grid[y][x]):
            no_up_trees = up_trees.index(tree)
    if no_up_trees == -1:
        no_up_trees = len(up_trees) -1
    print('Trees above: ' + str(up_trees[1:]) + ' (' + str(len(up_trees) - 1) + ' trees); viewing distance = '+str(no_up_trees))
    # down
    down_trees = ['-1']
    no_down_trees = -1
    for y_val in range(y+1, grid_height):
        down_trees.append(grid[y_val][x])
    for tree in down_trees[1:]:
        if int(tree) >= int(grid[y][x]):
            no_down_trees = down_trees.index(tree)
    if no_down_trees == -1:
        no_down_trees = len(down_trees) -1
    print('Trees below: ' + str(down_trees[1:]) + ' (' + str(len(down_trees) - 1) + ' trees); viewing distance = ' + str(no_down_trees))
    # left
    left_trees = ['-1']
    no_left_trees = -1
    for x_val in range(x-1,-1,-1):
        left_trees.append(grid[y][x_val])
    for tree in left_trees[1:]:
        if int(tree) >= int(grid[y][x]):
            no_left_trees = left_trees.index(tree)
    if no_left_trees == -1:
        no_left_trees = len(left_trees) -1
    print('Trees to the left: ' + str(left_trees[1:]) + ' (' + str(len(left_trees) - 1) + ' trees); viewing distance = ' + str(no_left_trees))
    # right
    right_trees = ['-1']
    no_right_trees = -1
    for x_val in range(x+1, grid_width):
        right_trees.append(grid[y][x_val])
    for tree in right_trees[1:]:
        if int(tree) >= int(grid[y][x]):
            no_right_trees = right_trees.index(tree)
    if no_right_trees == -1:
        no_right_trees = len(right_trees) - 1
    print('Trees to the right: ' + str(right_trees[1:]) + ' (' + str(len(right_trees) - 1) + ' trees); viewing distance = ' + str(no_right_trees))
    score = no_up_trees * no_down_trees * no_left_trees * no_right_trees
    return(score)


scenic_score(test_input,2,3)

max_scenic_score = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        max_scenic_score = max(scenic_score(input,x,y), max_scenic_score)

print(max_scenic_score)
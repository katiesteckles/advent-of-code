import copy
with open("2021/day13_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

dot_positions = []
folds = []
type = 'dots'
for line in input:
    if line == '':
        type = 'folds'
    if type == 'dots':
        dot_positions.append(list(map(int,line.split(','))))
    elif type == 'folds' and line != '':
        folds.append(line[11:].split('='))
        folds[-1][-1] = int(folds[-1][-1])

def apply_fold(grid, fold):
    grid_size = [max([griditem[0] for griditem in grid]), max([griditem[1] for griditem in grid])]
    print('Grid is '+ str(grid_size[0])+' wide and '+str(grid_size[1])+ ' high')
    if fold[0] == 'x':
        for point in grid:
            if point[0] > fold[1]:
                point[0] = (2*fold[1])-point[0]
    elif fold[0] == 'y':
        for point in grid:
            if point[1] > fold[1]:
                point[1] = (2*fold[1])-point[1]
    return grid

# part 1
foldable_version = copy.deepcopy(dot_positions)
folded_once = apply_fold(foldable_version,folds[0])

set_folded_once = set()
for point in folded_once:
    set_folded_once.add(tuple(point))

print(len(set_folded_once))
print(len(dot_positions))

# part 2

foldable_version_2 = copy.deepcopy(dot_positions)
for fold in folds:
    apply_fold(foldable_version_2, fold)

set_folded_up = set()
for point in foldable_version_2:
    set_folded_up.add(tuple(point))

folded_size = [max([griditem[0] for griditem in set_folded_up]), max([griditem[1] for griditem in set_folded_up])]

final_grid = []
for y in range(folded_size[0]+1):
    thisrow = ''
    for x in range(folded_size[1]+1):
        if (x,y) in set_folded_up:
            thisrow = thisrow+'#'
        else:
            thisrow = thisrow+' '
    final_grid.append(thisrow)

print('\n'.join(' '.join(map(str, sub)) for sub in final_grid))
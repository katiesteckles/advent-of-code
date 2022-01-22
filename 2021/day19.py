with open("2021/day19_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

scanners = []
for index, line in enumerate(input):
    list_number = -1
    if line[:3] == '---':
        list_number +=1
        scanners.append([])
    elif line != '':
        scanners[list_number].append([int(x) for x in line.split(',')])

orient_dict = {0: ['+0', '+1', '+2'],
               1: ['-1','+0','+2'],
               2: ['+1','-0','+2'],
               3: ['-2','+1','+0'],
               4: ['+2','+1','-0'],
               5: ['+0','+2','-1'],
               6: ['+0','-2','+1'],
               7: ['-0','-1','+2'],
               8: ['+0','-1','-2'],
               9: ['-0','+1','-2'],
               10: ['-0','+2','+1'],
               11: ['-0','-2','-1'],
               12: ['+2','-1','+0'],
               13: ['-2','-1','-0'],
               14: ['+1','+0','-2'],
               15: ['-1','-0','-2'],
               16: ['+1','+2','+0'],
               17: ['+1','-2','-0'],
               18: ['-1','+2','-0'],
               19: ['-1','-2','+0'],
               20: ['+2','+0','+1'],
               21: ['+2','-0','-1'],
               22: ['-2','+0','-1'],
               23: ['-2','-0','+1']}

def rotate(coords, orientation):
    rotation = orient_dict[orientation]
    newcoords = []
    for index, coord in enumerate(coords):
        newcoords.append(coords[int(rotation[index][1])])
        if rotation[index][0] == '-':
            newcoords[index] *= -1
    return newcoords

# test = [rotate([1,2,3],i) for i in range(24)]

def compare_scanners(fixed, rotating):
    for i in range(24):
        # print('Orientation: '+str(orient_dict[i]))
        all_oriented = [rotate(point,i) for point in rotating]
        for point_fixed in fixed:
            for point_rotating in rotating:
                point_oriented = rotate(point_rotating, i)
                difference = [points[0]-points[1] for points in zip(point_fixed, point_oriented)]
                #print('Difference: '+str(difference))
                all_oriented_shifted = [[points[0]+points[1] for points in zip(difference, oriented)] for oriented in all_oriented]
                matches = set([tuple(point) for point in all_oriented_shifted]) & set([tuple(point) for point in fixed])
                if len(matches) >= 12:
                    print('Found a match! '+str(matches))
                    return difference, i
    return('No matches')

match_set = []
for i in range(len(scanners)):
    for j in range(len(scanners)):
        if i != j:
            comparison = compare_scanners(scanners[i], scanners[j])
            print(str(i) + ', ' + str(j)+'; '+str(comparison))
            if comparison != 'No matches':
                match_set.append([comparison, i, j])

#compare_scanners(scanners[1], scanners[5])
#len(set([m[1] for m in match_set]+[m[2] for m in match_set]))

match_paths = {}
for i in range(32):
    match_paths[i] = set([match[1] for match in match_set if match[2] == i])

level_paths = {}
level_paths[0] = set([m[1] for m in match_set if m[2] == 0])
for i in range(31):
    level_paths[i+1] = set()
    for match in level_paths[i]:
        level_paths[i+1] |= set([m[1] for m in match_set if m[2] == match[0]])


import copy
breakable_scanners = copy.deepcopy(scanners)
breakable_paths = copy.deepcopy(match_paths)

def roll_up(x,y, deleted):
    x_match = [match[0] for match in match_set if match[1] == x and match[2] == y] # difference vec/orientation
    new_beacon_positions = []
    for beacon in breakable_scanners[x]:
        new_beacon_position = rotate(beacon, x_match[0][1])
        new_beacon_position = [point[0] + point[1] for point in zip(new_beacon_position, x_match[0][0])]
        new_beacon_positions.append(new_beacon_position)
    breakable_scanners[y] = list(set([tuple(b) for b in breakable_scanners[y]]+[tuple(n) for n in new_beacon_positions]))
    breakable_scanners[x] = []
    breakable_paths[y].remove(x)
    breakable_paths[x].remove(y)
    deleted.append(x)
    return deleted

deleted = []

solo_paths = [x for x in breakable_paths.keys() if len(breakable_paths[x]) == 1 and x not in deleted]
print(solo_paths)
for x in solo_paths:
    x_match = [match[2] for match in match_set if match[1] == x and match[2] not in deleted] # difference vec/orientation
    deleted = roll_up(x, x_match[0], deleted)

# custom shit
deleted = roll_up(23, 30, deleted)
deleted = roll_up(30, 4, deleted)
deleted = roll_up(24, 5, deleted)
deleted = roll_up(22, 28, deleted)
deleted = roll_up(19, 20, deleted)
deleted = roll_up(20, 17, deleted)
deleted = roll_up(17, 28, deleted)
deleted = roll_up(16, 9, deleted)
deleted = roll_up(13, 7, deleted)
deleted = roll_up(11, 5, deleted)
deleted = roll_up(9, 4, deleted)
deleted = roll_up(7, 10, deleted)
deleted = roll_up(3, 4, deleted)
deleted = roll_up(1, 5, deleted)
deleted = roll_up(4, 5, deleted)
deleted = roll_up(5, 10, deleted)
deleted = roll_up(10, 29, deleted)
deleted = roll_up(29, 2, deleted)
deleted = roll_up(2, 25, deleted)
deleted = roll_up(25, 8, deleted)
deleted = roll_up(8, 0, deleted)
deleted = roll_up(28, 0, deleted)
# 4 - 5 - 10 - 29 - 2 - 25 - 8 - 0

final_scanners = set([tuple(s) for s in breakable_scanners[0]])
len(final_scanners)

for i in range(32):
    if i not in deleted:
        print(i)
# Rotations:
# face 90, -90, 180 for each face (9) + 0
# 0	    o
# 1	    x>-y, y>x
# 2	    x>y, y>-x
# 3	    x>-z, z>x
# 4	    x>z, z>-x
# 5	    z>-y, y>z
# 6	    z>y, y>-z
# 7	    x>-x, y>-y
# 8	    y>-y, z>-z
# 9	    x>-x, z>-z
# edge 180 for each pair of edges  (6)
# 10    x>-x, y>z, z>y
# 11	x>-x, y>-z, z>-y
# 12	y>-y, x>z, z>x
# 13	y -y, x -z, z -x
# 14	z -z, xy, yx
# 15	z -z, x -y, y -x
# corners 120 and -120 for each pair of opposite corners (8)
# 16	xy, yz, zx
# 17	xy, y -z, z -x
# 18	x -y, yz, z-x
# 19	x -y, y -z, zx
# 20	xz, yx, zy
# 21	xz, y -x, z -y
# 22	x -z, yx, z -y
# 23	x -z, y-x, zy






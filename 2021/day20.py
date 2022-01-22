with open("2021/day20_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

enhancer = input[0]
image = input[2:]

def add_borders(grid, bg,thickness):
    width = len(grid[0])
    dotsstring = ''
    for i in range(width + (2*thickness)):
        dotsstring += bg
    new_grid = [dotsstring] * thickness
    for line in grid:
        new_grid.append(bg*thickness + line +bg*thickness)
    new_grid.extend([dotsstring]*thickness)
    return new_grid

add_borders(['row1','row2'],'.',2)

def find_square(grid, position, bg):
    #this bit just makes sure its in range
    new_grid = add_borders(grid, bg, 3)
    position[0] += 3
    position[1] += 3
    #this is the actual function
    #print(len(new_grid))
    square = [[],[],[]]
    for x in range(3):
        for y in range(3):
            square[y].append(new_grid[position[1]+y][position[0]+x])
    return square

#add_borders(breakable_image,'.')

find_square(image,[0,2],'.')
find_square(image,[2,98],'.')

def lookup_square(square, enhancer):
    sqstring = ''
    for row in square:
        for col in row:
            if col == '#':
                sqstring += '1'
            elif col == '.':
                sqstring += '0'
    value = int(sqstring,2)
    #print(sqstring+' = '+str(value))
    return enhancer[value]

lookup_square(find_square(image,[2,4]), enhancer)

import copy
breakable_image = copy.deepcopy(add_borders(image, '.',1))
print(len(breakable_image[0]),len(breakable_image))
iterated_grid = []
for y, line in enumerate(breakable_image):
    iterated_grid.append('')
    for x, pixel in enumerate(line):
        new_pixel = lookup_square(find_square(breakable_image,[x,y], '.'), enhancer)
        print(x, y, new_pixel)
        iterated_grid[y] += new_pixel

breakable_image = copy.deepcopy(add_borders(iterated_grid, '#',1))
print(len(breakable_image[0]),len(breakable_image))
iterated_grid2 = []
for y, line in enumerate(breakable_image):
    iterated_grid2.append('')
    for x, pixel in enumerate(line):
        new_pixel = lookup_square(find_square(breakable_image,[x,y], '#'), enhancer)
        print(x, y, new_pixel)
        iterated_grid2[y] += new_pixel

gridcounts = 0
for line in iterated_grid2:
    for char in line:
        if char == '#':
            gridcounts +=1

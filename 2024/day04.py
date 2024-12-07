with open("2024/day04.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

testinput = ['MMMSXXMASM','MSAMXMSMSA','AMXSXMAAMM','MSAMASMSMX','XMASAMXAMM','XXAMMXXAMA','SMSMSASXSS','SAXAMASAAA','MAMMMXMMMM','MXMXAXMASX']

def x_pokeout(x, y, input): # sorry
    number_of_xmases = 0
    # print(x,y)
    if input[y][x] != 'X':
        print("That's not an X")
    # check right
    if x+3 <= len(input[y])-1:
        if input[y][x+1] == 'M' and input[y][x+2] == 'A' and input[y][x+3] == 'S':
        number_of_xmases += 1
    # check left
    if x - 3 >= 0:
        if input[y][x-1] == 'M' and input[y][x-2] == 'A' and input[y][x-3] == 'S':
            number_of_xmases += 1
    # check down or up
    if y+3 <= len(input)-1:
        if input[y+1][x] == 'M' and input[y+2][x] == 'A' and input[y+3][x] == 'S':
            number_of_xmases += 1
    # check up or down
    if y - 3 >= 0:
        if input[y-1][x] == 'M' and input[y-2][x] == 'A' and input[y-3][x] == 'S':
            number_of_xmases += 1
    # check diagonals
    if x+3 <= len(input[y])-1 and y+3 <= len(input)-1:
        if input[y+1][x+1] == 'M' and input[y+2][x+2] == 'A' and input[y+3][x+3] == 'S':
            number_of_xmases += 1
    if x - 3 >= 0 and y - 3 >= 0:
        if input[y-1][x-1] == 'M' and input[y-2][x-2] == 'A' and input[y-3][x-3] == 'S':
            number_of_xmases += 1
    if x + 3 <= len(input[y])-1 and y - 3 >= 0:
        if input[y-1][x+1] == 'M' and input[y-2][x+2] == 'A' and input[y-3][x+3] == 'S':
            number_of_xmases += 1
    if x - 3 >= 0 and y+3 <= len(input)-1:
        if input[y+1][x-1] == 'M' and input[y+2][x-2] == 'A' and input[y+3][x-3] == 'S':
            number_of_xmases += 1
    return number_of_xmases

eckses = []
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == 'X':
            eckses.append([x,y])

total_xmas = 0
for ecks in eckses:
    total_xmas += x_pokeout(ecks[0],ecks[1],input)

print(total_xmas)

# Part B

# s s  s m  m m  m s
#  a    a    a    a
# m m  s m  s s  m s

corner_combos = [['S','S','M','M'], ['S','M','S','M'], ['M','M','S','S'], ['M','S','M','S']] #above left, above right, below left, below right

def sam_finder(x, y, input):
    number_of_xmases = 0
    # print(x, y)
    if input[y][x] != 'A':
        print("That's not an A")
    # check below right
    if x + 1 <= len(input[y]) - 1 and x - 1 >= 0 and y + 1 <= len(input) - 1 and y - 1 >= 0:
        # retrieve corners
        corners = [input[y-1][x-1],  input[y-1][x+1],  input[y+1][x-1], input[y+1][x+1]] #above left, above right, below left, below right
        if corners in corner_combos:
            number_of_xmases += 1
    return number_of_xmases

ayys = []
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == 'A':
            ayys.append([x,y])

total_x_mas = 0
for ay in ayys:
    total_x_mas += sam_finder(ay[0],ay[1],input)

print(total_x_mas)




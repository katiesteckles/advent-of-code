import copy
with open("2021/day04_input.txt", "r") as file:
    input = file.readlines()

numbers = copy.deepcopy(input[0]).split(',')
gridsonly = copy.deepcopy(input[2:])
grids = [[] for i in range(100)]

for i in range(len(gridsonly)):
    currentrow = gridsonly[i][:-1].split(" ")
    grids[int(i/6)].append([int(entry) for entry in currentrow if entry !=''])

for grid in grids:
    grid[-1] = '1111111111111111111111111'

teststring='0100001111010000100001000'

def checkgrid(gridstring):
    for i in range(5):
        if gridstring[5*i:(5*i)+5] == '00000':
            print('Winning line in row '+str(i)+'!')
            return True
    for j in range(5):
        if gridstring[j]+gridstring[5+j]+gridstring[10+j]+gridstring[15+j]+gridstring[20+j] == '00000':
            print('Winning line in column '+str(j)+'!')
            return True

def play_number(number, grids):
    winning_grids = []
    for gridnum, grid in enumerate(grids):
        for rownum in range(5):
            if number in grid[rownum]:
                colnum = grid[rownum].index(number)
                print(str(number)+' found in Grid '+str(gridnum)+' at position '+str(rownum)+', '+str(colnum))
                winning_grids.append([gridnum, rownum, colnum])
    return winning_grids

def tick_off_scores(winning_grids, grids):
    for winner in winning_grids:
        #print(winner)
        gridstring = grids[winner[0]][-1]
        winnerpos = (5*winner[1]) + winner[2]
        #print(winnerpos)
        newgridstring = gridstring[:winnerpos]+'0'+gridstring[(winnerpos+1):]
        grids[winner[0]][-1] = newgridstring

def calculate_score(lastnum, gridnum):
    winnah = []
    for i in range(5):
        winnah.extend(grids[gridnum][i])
    #print(winnah)
    #print(grids[gridnum][-1])
    total_score = 0
    for i in range(25):
        griddigit = grids[gridnum][-1][i]
        total_score += winnah[i]*int(griddigit)
    total_score *= lastnum
    return total_score


def do_thing():
    for i in range(len(numbers)):
        tick_off_scores(play_number(int(numbers[i]), grids), grids)
        for gridnum, grid in enumerate(grids):
            if checkgrid(grid[-1]):
                print('Winning line in grid '+str(gridnum))
                return [numbers[i], gridnum]

winning_grid = do_thing()
calculate_score(*winning_grid)

#Part 2

def do_thing2():
    list_of_winners = []
    for i in range(len(numbers)):
        tick_off_scores(play_number(int(numbers[i]), grids), grids)
        for gridnum, grid in enumerate(grids):
            if checkgrid(grid[-1]):
                print('Winning line in grid '+str(gridnum))
                if gridnum not in list_of_winners:
                    list_of_winners.append(gridnum)
                if len(list_of_winners) == 100:
                    return [numbers[i],list_of_winners[-1]]

last_to_win = do_thing2()
calculate_score(int(last_to_win[0]),last_to_win[1])
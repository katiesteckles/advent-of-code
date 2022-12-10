with open("2022/day10_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]
    input = [line.split(' ') for line in input]


with open("2022/test_input10.txt","r") as file:
    test_input = file.readlines()
    test_input = [line.strip() for line in test_input]
    test_input = [line.split(' ') for line in test_input]

command_lengths = {
    'noop': 1,
    'addx': 2
}

signal_strengths = 0
X = 1
cycle = 0

print('X = '+str(X))
for command in input:
    print(command)
    for i in range(command_lengths[command[0]]):
        cycle += 1
        print('Cycle ' + str(cycle) + '; X = ' + str(X))
        if (cycle-20) % 40 == 0:
            print('It is time! Cycle number '+str(cycle)+'; The value of X is '+str(X)+' so I will add ' + str(cycle*X))
            signal_strengths += (cycle * X)
            print('Total signal strength is now '+str(signal_strengths))
    if command[0] == 'addx':
        X += int(command[1])

print(signal_strengths)

# Part B

import copy

X = 1
cycle = 0

print('X = '+str(X))
drawn_pixels = []
fortydots = [' ']*40
for i in range(6): drawn_pixels.append(copy.deepcopy(fortydots))
for command in input:
    print(command)
    for i in range(command_lengths[command[0]]):
        cycle += 1
        row = int((cycle)/40)
        column = ((cycle-1) % 40)
        print('Cycle ' + str(cycle) + '; row '+str(row)+ ' column '+str(column) + '; X = ' + str(X))
        if column in {X - 1, X, X + 1}:
            print('Updating pixel in row '+str(row)+ ' column '+str(column))
            drawn_pixels[row][column] = '#'
    if command[0] == 'addx':
        X += int(command[1])

for i in range(6): print(''.join(drawn_pixels[i]))

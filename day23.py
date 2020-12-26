def iterate_cups(input):
    input_len = len(input)
    #print(str(input) + ' (length ' + str(input_len) + ')')
    # the first cup is the 'current cup'
    current_cup = input[0]
    # pop cups 2-4
    move_cups = [input.pop(1)]
    move_cups.append(input.pop(1))
    move_cups.append(input.pop(1))
    destination_cup = current_cup - 1
    if destination_cup == 0: destination_cup = input_len
    while destination_cup in move_cups:
        destination_cup = destination_cup - 1
        if destination_cup == 0: destination_cup = input_len
    #print('Moving cups ' + str(move_cups) + ' to after cup ' + str(destination_cup))
    # locate the destination cup
    found_place = 0
    while found_place == 0:
        for i in range(1, len(input)):
            if input[i] == destination_cup:
                # move cups 2,3,4 to there
                #print('Cup ' + str(destination_cup) + ' located in position ' + str(i+1))
                input = input[:i+1] + move_cups + input[i+1:]
                found_place = 1
                break
    # rotate cups so the next cup is first
    input.append(input.pop(0))
    return input

import copy
actual_input = [5,8,9,1,7,4,2,6,3]
test_input = [3,8,9,1,2,5,4,6,7]
test_input = iterate_cups(test_input)

input = copy.deepcopy(actual_input)
for i in range(100):
    input = iterate_cups(input)

# part 2

input = copy.deepcopy(actual_input)
input.append(len(input)+1)
for i in range(1000000-len(input)):
    input.append(input[-1] + 1)

for i in range(100):
    input = iterate_cups(input)
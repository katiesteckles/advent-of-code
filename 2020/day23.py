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

def dictify(input):
    cup_dict = {}
    cup_dict[input[0]] = [input[-1], input[1]]
    cup_dict[input[-1]] = [input[-2], input[0]]
    for i in range(1, len(input)-1):
        cup_dict[input[i]] = [input[i-1], input[i+1]] # add a line to the dictionary that has key that cup number and a pair (x-1, x+1) which are the things to its left and right
    return cup_dict

def dictiterate_cups(cup_dict, current_cup):
        input_len = len(cup_dict)
        move_cups = [cup_dict[current_cup][1],cup_dict[cup_dict[current_cup][1]][1],cup_dict[cup_dict[cup_dict[current_cup][1]][1]][1]]
        # print(move_cups)
        destination_cup = current_cup - 1
        # print(destination_cup)
        if destination_cup == 0: destination_cup = input_len
        while destination_cup in move_cups:
            destination_cup = destination_cup - 1
            if destination_cup == 0: destination_cup = input_len
        # set the current cup's right neighbour to be the third cup in move_cups' old right neighbour
        cup_dict[current_cup][1] = cup_dict[move_cups[-1]][1]
        # the third cup in move_cups' right neighbour to be the destination cup's current right neighbour
        cup_dict[move_cups[-1]][1] = cup_dict[destination_cup][1]
        # the destination cup's right neighbour's left neighbour to be the third cup in move_cups
        cup_dict[cup_dict[destination_cup][1]][0] = move_cups[-1]
        # set the destination cup's right neighbour to be the first in move_cups
        cup_dict[destination_cup][1] = move_cups[0]
        # set the first in move_cups' left neighbour to be the destination cup
        cup_dict[move_cups[1]][0] = destination_cup
        # rotate cups so the next cup is first
        current_cup = cup_dict[current_cup][1]
        return [cup_dict, current_cup]


def reassemble_cups(cup_dict, first_cup):
    cup_list = [first_cup]
    for i in range(len(cup_dict) - 1):
        cup_list.append(cup_dict[cup_list[-1]][1])
    print(cup_list)

actual_input = [5,8,9,1,7,4,2,6,3]

import copy
long_input = copy.deepcopy(actual_input)
long_input.append(len(long_input) + 1)
for i in range(1000000 - len(long_input)):
    long_input.append(long_input[-1] + 1)

# test_input = [3,8,9,1,2,5,4,6,7]
# cup_dict = dictify(actual_input)
# cup_dict = dictify(test_input)
cup_dict = dictify(long_input)
current_cup = long_input[0]

for i in range(10000000):
    [cup_dict, current_cup] = dictiterate_cups(cup_dict,current_cup)

# reassemble_cups(cup_dict,current_cup)

total = cup_dict[1][1] * cup_dict[cup_dict[1][1]][1]

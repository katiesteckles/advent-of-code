with open("2022/day05_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

import copy
from pprint import pprint

for i in range(len(input)):
    if input[i][0] == "1":
        number_of_lines = i


def read_in_crates(crates):
    line_length = len(crates[0])
    total_chunks = (line_length+1)/4
    chunked_lines = []
    for line in crates:
        chunks = []
        for i in range(int(total_chunks)):
            chunks.append(line[(4*i)+1:(4*i)+2])
        chunked_lines.append(chunks)
    return chunked_lines

crates = read_in_crates(input[:number_of_lines])

def flip_crates(crates):
    number_of_stacks = len(crates[-1])
    print(str(number_of_lines) + " lines; "+str(number_of_stacks)+ " stacks")
    flipped_crates = []
    for i in range(number_of_stacks):
        stack = []
        for j in range(number_of_lines):
            if crates[number_of_lines-j-1][i] != ' ':
                stack.append(crates[number_of_lines-j-1][i])
        flipped_crates.append(stack)
    return flipped_crates

flipped_crates = flip_crates(crates)

input = input[(number_of_lines+2):]

def perform_move_action_9000(crates, move_action):
    number_of_crates_to_move = int(move_action[5:move_action.find(' from')])
    move_from = int(move_action[move_action.find('from ')+5:move_action.find(' to')])
    move_to = int(move_action[move_action.find('to ') + 3:])
    print('move '+str(number_of_crates_to_move)+' from '+str(move_from)+' to '+str(move_to)+' (<< this should say "'+move_action+'")')
    for i in range(number_of_crates_to_move):
        crates[move_to-1].append(crates[move_from-1].pop())
    return crates


test_crates = copy.deepcopy(flipped_crates)
modify_crates = copy.deepcopy(flipped_crates)

# perform_move_action_9000(test_crates, input[0])

for line in input:
    perform_move_action_9000(modify_crates, line)

final_message = ''
for i in range(len(modify_crates)):
    final_message = final_message+(modify_crates[i][-1])

print(final_message)

# Part B
def perform_move_action_9001(crates, move_action):
    number_of_crates_to_move = int(move_action[5:move_action.find(' from')])
    move_from = int(move_action[move_action.find('from ')+5:move_action.find(' to')])
    move_to = int(move_action[move_action.find('to ') + 3:])
    print('move '+str(number_of_crates_to_move)+' from '+str(move_from)+' to '+str(move_to)+' (<< this should say "'+move_action+'")')
    crates[move_to - 1].extend(crates[move_from - 1][-number_of_crates_to_move:])
    crates[move_from - 1] = crates[move_from - 1][:-number_of_crates_to_move]
    pprint(crates)
    return crates

# perform_move_action_9001(test_crates, input[2])

modify2_crates = copy.deepcopy(flipped_crates)


for line in input:
    perform_move_action_9001(modify2_crates, line)

final_message2 = ''
for i in range(len(modify2_crates)):
    final_message2 = final_message2+(modify2_crates[i][-1])

print(final_message2)
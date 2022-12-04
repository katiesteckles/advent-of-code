with open("2022/day03_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]


def char_to_priority(char):
    if ord(char) > 96:
        return(ord(char)-96)
    else:
        return(ord(char)-38)


def items_to_priority_sets(items_list):
    items_0 = items_list[:int(len(items_list) / 2)]
    items_1 = items_list[int(len(items_list) / 2):]
    priority_sets = [[],[]]
    for i in range(len(items_0)):
        priority_sets[0].append(char_to_priority(items_0[i]))
    for i in range(len(items_1)):
        priority_sets[1].append(char_to_priority(items_1[i]))
    return priority_sets


def items_to_priority_set(items_list):
    priority_set = []
    for i in range(len(items_list)):
        priority_set.append(char_to_priority(items_list[i]))
    return priority_set


total = 0
for line in input:
    prio_sets = items_to_priority_sets(line)
    total += set(prio_sets[0]).intersection(set(prio_sets[1])).pop()

print(total)

# Part B (ugh)

lines_remaining = len(input)
sets_of_three = [[]]
current_set = 0
while lines_remaining != 0:
    if lines_remaining % 3 != 1:
        sets_of_three[current_set].append(items_to_priority_set(input[len(input)-lines_remaining]))
        lines_remaining -= 1
    elif lines_remaining % 3 == 1:
        sets_of_three[current_set].append(items_to_priority_set(input[len(input) - lines_remaining]))
        lines_remaining -= 1
        current_set += 1
        sets_of_three.append([])
sets_of_three = sets_of_three[:-1]

import copy
total = 0
for set_of_three in sets_of_three:
    this_set = copy.deepcopy(set_of_three)
    this_set = [set(this_set[i]) for i in range(3)]
    this_set[0].intersection_update(this_set[1], this_set[2])
    total += this_set[0].pop()

print(total)
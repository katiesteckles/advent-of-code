import copy
import re
with open("day18_input.txt", "r") as file:
    lines = file.readlines()

lines = [line[:-1] for line in lines]

def resolve_lr(input_string): # the input string should not contain brackets
    input_string = input_string.split(' ')
    while len(input_string) > 1:
        if input_string[1] == '+':
            numand = int(input_string[0]) + int(input_string[2])
            input_string = input_string[2:]
            input_string[0] = numand
        elif input_string[1] == '*':
            numand = int(input_string[0]) * int(input_string[2])
            input_string = [numand] + input_string[3:]
    return input_string[0]


def resolve_addpriority(input_string): # the input string should not contain brackets
    input_string = input_string.split(' ')
    while input_string.count('+') > 0:
        firstadd = input_string.index('+')
        numand = int(input_string[firstadd-1]) + int(input_string[firstadd+1])
        input_string = input_string[:firstadd-1] + [numand] + input_string[firstadd+2:]
        print(input_string)
    while len(input_string) > 1:
        numand = int(input_string[0]) * int(input_string[2])
        input_string = [numand] + input_string[3:]
        print(input_string)
    return input_string[0]

#resolve_lr('3 * 2 + 2')
#resolve_addpriority('3 * 2 + 2 * 6 + 5')

bracket_group_regex = re.compile('(\\([0-9\\s\\+\\*]*\\))')

def parse_line(line,bodmastype):
    line_in_progress = copy.deepcopy(line)
    brackets = line_in_progress.count('(')
    while brackets > 0:
        position = bracket_group_regex.search(line_in_progress).span()
        stringo = line_in_progress[position[0]+1:position[1]-1]
        print(position, stringo)
        parsed = line_in_progress[:position[0]] + str(bodmastype(stringo)) + line_in_progress[position[1]:]
        line_in_progress = parsed
        print(line_in_progress)
        brackets = line_in_progress.count('(')
    return bodmastype(line_in_progress)

total = 0
for line in lines:
    total += parse_line(line,resolve_addpriority)


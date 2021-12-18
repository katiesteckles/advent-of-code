import copy
with open("2021/day18_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

def characterise(line):
    return [char for char in line if char != ',']

input_chars = [characterise(line) for line in input]
test_number = copy.deepcopy(input_chars[0])

def snailsum(list_of_things_to_add):
    to_add = [thing for thing in list_of_things_to_add]
    return reduce(to_add)

def find_next_regular(whole_number, reg_find_pos, direction):
    if direction == 'left':
        for i in range(reg_find_pos-1, -1, -1):
            if whole_number[i] not in '[]':
                return i, whole_number[i]
        return 'Nope'
    if direction == 'right':
        for i in range(reg_find_pos+1, len(whole_number)):
            if whole_number[i] not in '[]':
                return i, whole_number[i]
        return 'Nope'

find_next_regular(input_chars[0],3,'right')

def is_explods(whole_number):
    print(whole_number)
    brackets = [[index, char] for index, char in enumerate(whole_number) if char in '[]']
    open_brackets = []
    for bracket in brackets:
        if bracket[1] == '[':
            open_brackets.append(bracket[1])
            if open_brackets[-5:] == ['[', '[', '[', '[', '[']:
                return True, bracket[0]
        if bracket[1] == ']':
            open_brackets = open_brackets[:-1]
    return False, 0
    #returns true/false and the location of the first bracket in the first one yo

def is_splits(whole_number):
    for index, char in enumerate(whole_number):
        if char not in '[]' and int(char) > 9:
            return True, index
    return False, 0
    # return true/false and the location of the first one

def reduce(whole_number):
    while True:
        explods = is_explods(whole_number)
        spliits = is_splits(whole_number)
        if explods[0]:
            whole_number = explode(whole_number, explods[1])
        elif spliits[0]:
            whole_number = split(whole_number, spliits[1])
        else:
            return(whole_number)

def explode(whole_number, pair_pos):
    if whole_number[pair_pos+1] not in '[]' and whole_number[pair_pos+2] not in '[]':
        left_num = find_next_regular(whole_number, pair_pos, 'left')
        right_num = find_next_regular(whole_number, pair_pos+3, 'right')
        if left_num != 'Nope': whole_number[left_num[0]] = str(int(left_num[1]) + int(whole_number[pair_pos + 1]))
        if right_num != 'Nope': whole_number[right_num[0]] = str(int(right_num[1]) + int(whole_number[pair_pos + 2]))
        whole_number = whole_number[:pair_pos] + ['0'] + whole_number[pair_pos+4:]
    else:
        print('Not a valid pair')
    return whole_number

# test_number = explode(test_number, 2)

def split(whole_number, splititem_pos):
    if whole_number[splititem_pos] not in '[]':
        splitter = int(whole_number[splititem_pos])
        splitted = ['[']
        splitted.append(str(splitter//2))
        splitted.append(str(splitter - (splitter // 2)))
        splitted.append(']')
        print(splitted)
        whole_number = whole_number[:splititem_pos] + splitted + whole_number[splititem_pos+1:]
    else:
        print('Not valid splittable')
    return whole_number

# test_number = split(test_number,6)

def calculate_magnitude(whole_number):
    while '[' in whole_number:
        for i in range(len(whole_number)-1):
            if whole_number[i] not in '[]' and whole_number[i+1] not in '[]':
                new_term = str(((3*int(whole_number[i])) + (2*int(whole_number[i+1]))))
                whole_number = whole_number[:i-1] + [new_term] + whole_number[i+3:]
                # print(whole_number)
                break
    return whole_number

while len(input_chars) > 1:
    input_chars = [snailsum(['[']+input_chars[0]+input_chars[1]+[']'])] + input_chars[2:]

part1ans = calculate_magnitude(input_chars[0])[0]

# Part 2

input_for_p2 = [characterise(line) for line in input]

mangoes = []
for line1 in input_for_p2:
    for line2 in input_for_p2:
        mangoes.append(int(calculate_magnitude(snailsum(['['] + line1 + line2 + [']']))[0]))

print(max(mangoes))
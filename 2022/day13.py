with open("2022/day13_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

pairs = []
no_pairs = int((len(input)+1)/3)
for i in range(150):
    pairs.append([eval(input[3*i]),eval(input[3*i+1])])

with open("2022/test_input_13.txt","r") as file:
    testinput = file.readlines()
    testinput = [line.strip() for line in testinput]

testpairs = []
no_testpairs = int((len(testinput)+1)/3)
for i in range(no_testpairs):
    testpairs.append([eval(testinput[3*i]),eval(testinput[3*i+1])])

def pair_compare(pair):
    ordered_flag = 0
    if type(pair[0]) == int and type(pair[1]) == int:
        # print('Two ints!')
        if pair[0] < pair[1]:
            ordered_flag = 1
            return ordered_flag
        elif pair[0] > pair[1]:
            ordered_flag = -1
            return ordered_flag
    if type(pair[0]) == int and type(pair[1]) == list:
        # print('One int, one list!')
        pair[0] = [pair[0]]
    if type(pair[0]) == list and type(pair[1]) == int:
        # print('One list, one int!')
        pair[1] = [pair[1]]
    if type(pair[0]) == list and type(pair[1]) == list:
        # print('Two lists!')
        for i in range(min(len(pair[0]),len(pair[1]))):
            if pair_compare([pair[0][i], pair[1][i]]) != 0:
                ordered_flag = pair_compare([pair[0][i], pair[1][i]])
                return ordered_flag
        if len(pair[0]) < len(pair[1]):
            ordered_flag = 1
            return ordered_flag
        elif len(pair[0]) > len(pair[1]):
            ordered_flag = -1
            return ordered_flag
    # print(str(pair) + ': ' + str(ordered_flag))
    return ordered_flag

total = 0
for pair in pairs:
    # print(str(pairs.index(pair)))
    if pair_compare(pair) == 1:
        total += pairs.index(pair)+1

print(total)

# Part B

import functools

all_things = [eval(line) for line in input if line != '']
all_things.extend([[[2]],[[6]]])

def stupid_compare(item1,item2):
    return -(pair_compare([item1,item2]))

sorted_things = sorted(all_things, key=functools.cmp_to_key(stupid_compare)) # wtf is this

value1 = sorted_things.index([[2]])+1
value2 = sorted_things.index([[6]])+1

print(value1*value2)
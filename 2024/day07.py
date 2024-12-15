with open("2024/day07.txt", "r") as file:
    input = file.readlines()
    input = [line.strip().split(': ') for line in input]

import copy

inted = []
for line in input:
    line_inted = [int(line[0]), line[1].split(' ')]
    line_inted[1] = [int(thing) for thing in line_inted[1]]
    inted.append(line_inted)

ops = [lambda x, y: x + y, lambda x, y: x * y]  # ops[0] is addition, ops[1] is multiplication

test_input = [[190, [10, 19]], [3267, [81, 40, 27]], [83, [17, 5]], [156, [15, 6]], [7290, [6, 8, 6, 15]], [161011, [16, 10, 13]], [192, [17, 8, 14]], [21037, [9, 7, 18, 13]], [292, [11, 6, 16, 20]]]

def check_ops(line, ops):
    num_inputs = len(line)
    results = []
    for i in range(2 ** (num_inputs-1)):
        currentline = copy.deepcopy(line)
        op_list = bin(i)[2:].zfill(num_inputs-1)
        #print(op_list)
        for op in op_list:
            input0 = currentline.pop(0)
            input1 = currentline.pop(0)
            currentline = [ops[int(op)](input0, input1)] + currentline
            # print(op, currentline)
        results.append([op_list, currentline[0]])
    return results

winners = []
for line in inted:
    ways = check_ops(line[1], ops)
    if line[0] in [way[1] for way in ways]:
        winners.append([line, [way for way in ways if way[1] == line[0]]])

total = sum([winner[0][0] for winner in winners])
print(total)

# Part B

new_ops = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))]  # ops[0] is addition, ops[1] is multiplication, ops[2] is concatenation

def to_base(number, base):
    if not number:
        return [0]
    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return list(reversed(digits))


def check_three_ops(line, ops):
    num_inputs = len(line)
    results = []
    for i in range(3 ** (num_inputs-1)):
        currentline = copy.deepcopy(line)
        op_list = ''.join([str(x) for x in to_base(i,3)]).zfill(num_inputs-1)
        #print(op_list)
        for op in op_list:
            input0 = currentline.pop(0)
            input1 = currentline.pop(0)
            currentline = [ops[int(op)](input0, input1)] + currentline
            #print(op, currentline)
        results.append([op_list, currentline[0]])
    return results

bwinners = []
for line in inted:
    # print(inted.index(line))
    bways = check_three_ops(line[1], new_ops)
    if line[0] in [way[1] for way in bways]:
        bwinners.append([line, [way for way in bways if way[1] == line[0]]])

btotal = sum([bwinner[0][0] for bwinner in bwinners])
print(btotal)
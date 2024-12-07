with open("2024/day05.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

rules = [[int(x) for x in pair.split('|')] for pair in input[:1176]]
lists = [[int(x) for x in printable.split(',')] for printable in input[1177:]]

testrules = [[47, 53], [97, 13], [97, 61], [97, 47], [75, 29], [61, 13], [75, 53], [29, 13], [97, 29], [53, 29],
             [61, 53], [97, 53], [61, 29], [47, 13], [75, 47], [97, 75], [47, 61], [75, 61], [47, 29], [75, 13],
             [53, 13]]
testlists = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29],
             [97, 13, 75, 29, 47]]


def printable_check(printable, rules):
    for i in range(len(printable)):
        # for the ith item in the list, check that the entries opposite that in the rules are not to the left of it in the ordering
        for rule in rules:
            if rule[0] == printable[i] and rule[1] in printable[:i]:
                # print(printable)
                # print(printable[i])
                # print('Need ' + str(rule) + ' but ' + str(printable[:i + 1]))
                # print('--')
                return [False, rule]
    return [True, printable]


number_printable = 0
for i in range(len(lists)):
    if printable_check(lists[i], rules)[0] == True:
        number_printable += lists[i][int((len(lists[i])+1)/2)-1]

print(number_printable)

# Part B

import copy

trules = copy.deepcopy(testrules)
tlists = copy.deepcopy(testlists)

# tnumber_sorted_printable = 0
# for i in range(len(tlists)):
#     if printable_check(tlists[i], trules)[0] == False:
#         while printable_check(tlists[i], trules)[0] == False:
#             fix = printable_check(tlists[i],trules)[1]
#             # take the item at fix[1] and place it after the instance of fix[0] in lists[i]
#             mover = tlists[i].pop(tlists[i].index(fix[1]))
#             print('Moving '+str(mover)+' to after '+str(fix[0])+' in list '+str(tlists[i]))
#             tlists[i].insert(tlists[i].index(fix[0])+1, mover)
#         tnumber_sorted_printable += tlists[i][int((len(tlists[i])+1)/2)-1]

number_sorted_printable = 0
for i in range(len(lists)):
    # print(str(i)+' of '+str(len(lists))) # haha this takes a while to run
    if printable_check(lists[i], rules)[0] == False:
        while printable_check(lists[i], rules)[0] == False:
            fix = printable_check(lists[i],rules)[1]
            # take the item at fix[1] and place it after the instance of fix[0] in lists[i]
            mover = lists[i].pop(lists[i].index(fix[1]))
            # print('Moving '+str(mover)+' to after '+str(fix[0])+' in list '+str(lists[i]))
            lists[i].insert(lists[i].index(fix[0])+1, mover)
        number_sorted_printable += lists[i][int((len(lists[i])+1)/2)-1]

print(number_sorted_printable)
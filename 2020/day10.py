import copy
import math
with open("day10_input.txt", "r") as file:
    numbers = file.readlines()

numbers = [int(number[:-1]) for number in numbers]

numbers_sorted = copy.deepcopy(numbers)
numbers_sorted.sort()

threes = 0
ones = 0
for i in range(len(numbers_sorted)-1):
    if numbers_sorted[i+1] - numbers_sorted[i] == 3:
        threes += 1
    elif numbers_sorted[i+1] - numbers_sorted[i] == 1:
        ones += 1

(threes+1) * (ones+1) # including the jump from 0 to the first one, and from the last one to the top

run_ways = [[1, 1], [2, 1], [3, 2], [4, 4], [5, 7], [6, 13]]
run_ways_dict = dict(run_ways)

    # 3: 2, 11
    # 4: 3, 12, 21, 111
    # 5: 13, 31, 22, 112, 121, 211, 1111
    # 6: 32, 23, 113, 131, 311, 221, 212, 122, 1112, 1121, 1211, 2111, 11111

# find the longest run
longest_run = 0
current_run = 0
for i in range(len(numbers_sorted)-1):
    if numbers_sorted[i+1] == numbers_sorted[i] + 1:
        current_run +=1
    else:
        if current_run > longest_run:
            longest_run = current_run
        current_run = 0

numbers_sorted_augmented = [0] + numbers_sorted + [numbers_sorted[-1]+3]

current_run = 1
runs = []
for i in range(len(numbers_sorted_augmented)-1):
    if numbers_sorted_augmented[i+1] == numbers_sorted_augmented[i] + 1:
        current_run +=1
    else:
        runs.append(current_run)
        current_run = 1

run_combos = [run_ways_dict[run] for run in runs]

product_so_far = 1
for combo in run_combos:
    product_so_far = product_so_far * combo

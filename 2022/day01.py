with open("2022/day01_input.txt", "r") as file:
    input = file.readlines()
    input = [item[:-1] for item in input]

elf_carries = [[]]
elf = 0
for i in range(len(input)):
    if input[i] == "":
        elf = elf + 1
        elf_carries.append([])
    else:
        elf_carries[elf].append(input[i])

elf_totals = []
for elf_instance in elf_carries:
    elf_intstance = [int(item) for item in elf_instance]
    elf_totals.append(sum(elf_intstance))

max(elf_totals)

import copy
sorted_totals = copy.deepcopy(elf_totals)
sorted_totals.sort()
top_three = sorted_totals[-3:]

sum(top_three)
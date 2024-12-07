with open("2024/day03.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

import re
muls = []
for i in range(6):
    muls.extend(re.findall('mul\([0-9]+,[0-9]+\)',input[i]))

multotal = 0
for mul in muls:
    mul = mul.split('(')[1].split(',')
    mul[1] = mul[1][:-1]
    multotal += (int(mul[0]) * int(mul[1]))

print(multotal)

# Part B

wholeinput = ''.join(input)

dosections = wholeinput.split('do()')

muls_b = []
for section in dosections:
    section = section.split("don't()")
    muls_b.extend(re.findall('mul\([0-9]+,[0-9]+\)',section[0]))

mulbtotal = 0
for mul in muls_b:
    mul = mul.split('(')[1].split(',')
    mul[1] = mul[1][:-1]
    mulbtotal += (int(mul[0]) * int(mul[1]))

print(mulbtotal)


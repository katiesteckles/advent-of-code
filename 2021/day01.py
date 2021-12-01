with open("2021/day01_input.txt", "r") as file:
    numbers = file.readlines()

nums_int = [int(x[:-1]) for x in numbers]

# part 1

incdecs = []
for i in range(len(nums_int)):
    if nums_int[i] > nums_int[i-1]:
        incdecs.append(1)
    else:
        incdecs.append(0)

totalincs = sum(incdecs)

# part 2

incdecs2 = []
for i in range(len(numbers_int)-2):
    if (nums_int[i+2]) > (nums_int[i-1]):
        incdecs2.append(1)
    else:
        incdecs2.append(0)

totalincs2 = sum(incdecs2)
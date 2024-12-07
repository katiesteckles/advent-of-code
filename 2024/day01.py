with open("2024/day01.txt", "r") as file:
    input = file.readlines()
    input = [[line.strip().split(" ")[0], line.strip().split(" ")[-1]] for line in input]

list1 = [int(x[0]) for x in input]
list2 = [int(x[1]) for x in input]

list1.sort()
list2.sort()

totaldiff = 0
for i in range(len(input)):
    totaldiff += abs(list1[i] - list2[i])

print(totaldiff)

# Part B

total = 0
for i in range(len(input)):
    total += list1[i]*list2.count(list1[i])

print(total)
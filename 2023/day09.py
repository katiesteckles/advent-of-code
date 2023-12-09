with open("2023/day09_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip().split(' ') for line in input]

input = [[int(x) for x in line] for line in input]

def find_next_item(list0):
    differences = [list0]
    while not all(value == 0 for value in differences[-1]):
        new_diffs = []
        for i in range(len(differences[-1])-1):
            new_diffs.append(differences[-1][i+1] - differences[-1][i])
        differences.append(new_diffs)
    # final bit where you find the end ones
    differences[-1].append(0)
    for i in range(len(differences)-2,-1,-1):
        differences[i].append(differences[i][-1] + differences[i+1][-1])
    return differences[0][-1]

test_input = [[0, 3, 6, 9, 12, 15],[1, 3, 6, 10, 15, 21],[10, 13, 16, 21, 30, 45]]

total = 0
for line in input:
    total += find_next_item(line)

print(total)

# Part 2

def find_prev_item(list0):
    differences = [list0]
    while not all(value == 0 for value in differences[-1]):
        new_diffs = []
        for i in range(len(differences[-1])-1):
            new_diffs.append(differences[-1][i+1] - differences[-1][i])
        differences.append(new_diffs)
    # final bit where you find the end ones
    differences[-1] = [0] + differences[-1]
    for i in range(len(differences)-2,-1,-1):
        differences[i] = [differences[i][0] - differences[i+1][0]] + differences[i]
    return differences[0][0]

ptotal = 0
for line in input:
    ptotal += find_prev_item(line)

print(ptotal)
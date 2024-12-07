with open("2024/day02.txt", "r") as file:
    input = file.readlines()
    input = [line.strip().split(' ') for line in input]

intput = []
for line in input:
    intput.append([int(item) for item in line])

def butisitsafe(list):
    if list[1] - list[0] > 0:
        for i in range(len(list)-1):
            if list[i+1] - list[i] < 1 or list[i+1] - list[i] > 3:
                return False
    elif list[1] - list[0] < 0:
        for i in range(len(list)-1):
            if list[i] - list[i+1] < 1 or list[i] - list[i+1] > 3:
                return False
    elif list[1] - list[0] == 0:
        return False
    return True

safelines = 0
for line in intput:
    if butisitsafe(line):
        safelines += 1

print(safelines)

# Part B

def checkandchuck(list):
    if butisitsafe(list):
        return True
    else:
        for i in range(len(list)):
            chucked = list[:i]+list[i+1:]
            if butisitsafe(chucked):
                return True
    return False

dampened_safelines = 0
for line in intput:
    if checkandchuck(line):
        dampened_safelines += 1

print(dampened_safelines)
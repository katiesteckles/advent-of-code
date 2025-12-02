with open("2025/day02.txt", "r") as file:
    input = file.readlines()[0].split(",")
    input = [line.split("-") for line in input]

input[-1][1] = input[-1][1][:-1]  # for some reason there's a \n there

#  testinput = [[11, 22], [95, 115],[998,1012],[1188511880,1188511890],[222220,222224], [1698522,1698528],[446443,446449],[38593856,38593862],[565653,565659], [824824821,824824827],[2121212118,2121212124]]

def expand_input(input):
    for i in range(len(input)):
        length = int(input[i][1]) - int(input[i][0])
        line = [int(input[i][0])]
        for j in range(length):
            line.append(line[-1]+1)
        input[i] = line
    return input

input = expand_input(input)
# testinput = expand_input(testinput)

def count_doubles(input):
    counter = 0
    for line in input:
        for i in range(len(line)):
            if len(str(line[i])) % 2 == 0:
                # print(str(line[i]))
                digits = int(len(str(line[i]))/2)
                if str(line[i])[:digits] == str(line[i])[digits:]:
                    # print(line[i])
                    counter += line[i]
    return counter

print(count_doubles(input))
# count_doubles(testinput)

# Part 2
def string_split(stirng, n):
    sections = []
    if len(stirng) % n == 0:
        for i in range(int(len(stirng)/n)):
            sections.append(stirng[n*i:n*(i+1)])
    return sections

def multicount(input):
    multimatches = []
    for line in input:
        for i in range(len(line)):
            for n in range(1,len(str(line[i]))):
                if len(str(line[i])) % n == 0:
                    # print(str(line[i]))
                    chunks = int(len(str(line[i])) / n)
                    sections = string_split(str(line[i]), n)
                    if len(set(sections)) == 1:
                        # print(line[i], chunks)
                        multimatches.append(line[i])
    return sum(set(multimatches))

print(multicount(input))
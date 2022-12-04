with open("2022/day04_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]


def list_of_sections(line):
    endpoints = [pair.split("-") for pair in line.split(",")]
    sections_0 = [i for i in range(int(endpoints[0][0]), int(endpoints[0][1])+1)]
    sections_1 = [i for i in range(int(endpoints[1][0]), int(endpoints[1][1])+1)]
    return [sections_0, sections_1]


contained = 0
for line in input:
    if set(list_of_sections(line)[0]).intersection(set(list_of_sections(line)[1])) == set(list_of_sections(line)[0]):
        contained += 1
    elif set(list_of_sections(line)[0]).intersection(set(list_of_sections(line)[1])) == set(list_of_sections(line)[1]):
        contained += 1

print(contained)

# Part B

intersected = 0
for line in input:
    if set(list_of_sections(line)[0]).intersection(set(list_of_sections(line)[1])) != set():
        intersected += 1

print(intersected)
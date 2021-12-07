import copy
with open("2021/day06_input.txt", "r") as file:
    input = file.readlines()

fish = list(map(int, input[0][:-1].split(',')))

fish_max = 6
newfish_max = 8

def iterate_day(fish_list):
    currentfishlength = len(fish_list)
    for i in range(currentfishlength):
        if fish_list[i] == 0:
            fish_list.append(newfish_max)
            fish_list[i] = fish_max
        else:
            fish_list[i] -= 1
    return(fish_list)

# test_fish = [1, 2, 3, 4, 0]
# iterate_day(test_fish)

fish_breakable = copy.deepcopy(fish)

for i in range(80):
    iterate_day(fish_breakable)
    print(len(fish_breakable))

# part 2

fish_ages = {}
for i in range(newfish_max + 1):
    fish_ages[i] = 0

def read_in_fish_ages(fish_list, dict):
    for fish in fish_list:
        dict[fish] += 1

read_in_fish_ages(fish,fish_ages)

def iterate_day_cheap(fish_dict):
    current_values = [fish_dict[i] for i in range(newfish_max+1)]
    for i in range(newfish_max):
        fish_dict[i] = current_values[i+1]
    fish_dict[fish_max] += current_values[0]
    fish_dict[newfish_max] = current_values[0]
    return(fish_dict)

for i in range(256):
    iterate_day_cheap(fish_ages)

print(sum(fish_ages.values()))
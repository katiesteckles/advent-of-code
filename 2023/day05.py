with open("2023/day05_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

seeds = [int(x) for x in input[0][7:].split(' ')]

types = {  # mainly used in debugging print statements
    0: 'seed',
    1: 'soil',
    2: 'fert',
    3: 'water',
    4: 'light',
    5: 'temp',
    6: 'hum',
    7: 'loc'
}

t_seeds = [79, 14, 55, 13]

test_maps = [['50 98 2','52 50 48'], ['0 15 37','37 52 2','39 0 15'], ['49 53 8','0 11 42','42 0 7','57 7 4'], ['88 18 7','18 25 70'], ['45 77 23','81 45 19','68 64 13'], ['0 69 1','1 0 69'], ['60 56 37','56 93 4']]

all_them_maps = [input[3:40], input[42:52], input[54:90], input[92:138], input[140:168], input[170:210], input[212:254]]

# ranges should look like: start of input range, end of input range, start of output range

def convert_range(range):
    values = [int(x) for x in range.split()]
    return [values[1], values[1]+values[2]-1, values[0]]

all_them_new_maps = [[],[],[],[],[],[],[]]
for i in range(7):
    for j in range(len(all_them_maps[i])):
        all_them_new_maps[i].append(convert_range(all_them_maps[i][j]))

new_test_maps = [[],[],[],[],[],[],[]]
for i in range(7):
    for j in range(len(test_maps[i])):
        new_test_maps[i].append(convert_range(test_maps[i][j]))

def feed_through_data(input_type, value, maps):
    for range_values in maps[input_type]:
        if range_values[0] <= value <= range_values[1]:
            return range_values[2] + value - range_values[0]
    return value

test_locations = []
for seed in t_seeds:
    latest_value = seed
    for i in range(7):
        latest_value = feed_through_data(i, latest_value, new_test_maps)
    test_locations.append(latest_value)


locations = []
for seed in seeds:
    latest_value = seed
    for i in range(7):
        latest_value = feed_through_data(i, latest_value, all_them_new_maps)
    locations.append(latest_value)

min(locations)

# Part 2

# No
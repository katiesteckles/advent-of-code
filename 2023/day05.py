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

# ranges should look like: start of input range, end of input range, offset to output range

def convert_range(range):
    values = [int(x) for x in range.split()]
    return [values[1], values[1]+values[2]-1, values[0]-values[1]]

all_them_new_maps = [[],[],[],[],[],[],[]]
for i in range(7):
    for j in range(len(all_them_maps[i])):
        all_them_new_maps[i].append(convert_range(all_them_maps[i][j]))
    all_them_new_maps[i].sort()

new_test_maps = [[],[],[],[],[],[],[]]
for i in range(7):
    for j in range(len(test_maps[i])):
        new_test_maps[i].append(convert_range(test_maps[i][j]))
    new_test_maps[i].sort()

def feed_through_data(input_type, value, maps):
    for range_values in maps[input_type]:
        if range_values[0] <= value <= range_values[1]:
            return range_values[2] + value
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
seed_ranges = []
for i in range(0,len(seeds),2):
    seed_ranges.append((int(seeds[i]),int(seeds[i])+int(seeds[i+1])-1))

t_seed_ranges = []
for i in range(0,len(t_seeds),2):
    t_seed_ranges.append((int(t_seeds[i]),int(t_seeds[i])+int(t_seeds[i+1])-1))

def determine_overlapping_ranges(input_range,sorted_maps):
    location_data = [[],[]]
    new_ranges = []
    if input_range[0] < sorted_maps[0][0]:
        if input_range[1] < sorted_maps[0][0]:
            return([input_range])
        new_ranges.append((input_range[0], sorted_maps[0][0] - 1))
        input_range = (sorted_maps[0][0], input_range[1])
    for j in range(2):
        for i in range(len(sorted_maps)-1):
            if sorted_maps[i][0] <= input_range[j] <= sorted_maps[i][1]: # if it's in an interval
                location_data[j] = [i, 'in']
            if sorted_maps[i][1] <= input_range[j] <= sorted_maps[i+1][0]: # if it's between an interval and the next one
                location_data[j] = [i, 'out']
        if sorted_maps[-1][0] <= input_range[j] <= sorted_maps[-1][1]:
            location_data[j] = [len(sorted_maps)-1, 'in']
        elif input_range[j] > sorted_maps[-1][1]:
            location_data[j] = [len(sorted_maps)-1, 'out']
    # location data is now: which interval the start is in (and whether it's in or past it) and then which interval the end is in (and whether it's in or past it)
    #print(location_data)
    i1 = location_data[0][0]  # interval numbers
    i2 = location_data[1][0]
    t1 = location_data[0][1]  # 'in' or 'out'
    t2 = location_data[1][1]
    if i1 == i2:
        if t1 == 'in':
            if t2 == 'in': # it's inside an interval
                new_ranges.append((input_range[0] + sorted_maps[i1][2], input_range[1] + sorted_maps[i1][2])) # find the image of the sub interval under the map into the next layer
            elif t2 == 'out':
                new_ranges.append((input_range[0] + sorted_maps[i1][2], sorted_maps[i1][1] + sorted_maps[i1][2]))
                new_ranges.append((sorted_maps[i1][1] + 1, input_range[1]))
        if t1 == 'out': # it's in one gap
            new_ranges.append(input_range)
    else:
        # horrific overlapping case
        # front parts
        if t1 == 'in':
            new_ranges.append((input_range[0] + sorted_maps[i1][2], sorted_maps[i1][1] + sorted_maps[i1][2]))  # from start of input range to end of first interval, shifted by interval value [2]
            if sorted_maps[i1][1]+1 != sorted_maps[i1+1][0]:
                new_ranges.append((sorted_maps[i1][1]+1, sorted_maps[i1+1][0]-1)) # also the corresponding out, but not shifted
        elif t1 == 'out':
            new_ranges.append((input_range[0], sorted_maps[i1+1][0]-1)) # from start of input range to start of interval after first interval, not shifted
        # middle parts
        for k in range(i1+1, i2): # the number of full intervals it overlaps
            new_ranges.append((sorted_maps[k][0] + sorted_maps[k][2], sorted_maps[k][1] + sorted_maps[k][2]))  # do the in
            if sorted_maps[k][1]+1 != sorted_maps[k+1][0]:
                new_ranges.append((sorted_maps[k][1]+1, sorted_maps[k+1][0]-1))  # do the next one out
        # endy parts
        if t2 == 'in':
            new_ranges.append((sorted_maps[i2][0] + sorted_maps[i2][2], input_range[1] + sorted_maps[i2][2]))  # from start of last interval to end of input range, shifted by interval value [2]
        elif t2 == 'out':
            new_ranges.append((sorted_maps[i2][0] + sorted_maps[i2][2], sorted_maps[i2][1] + sorted_maps[i2][2]))  # the whole of the last interval
            new_ranges.append((sorted_maps[i2][1]+1, input_range[1]))  # from end of last interval to end input range, not shifted
    #print(new_ranges)
    return new_ranges

determine_overlapping_ranges([90,105], new_test_maps[0])

# test version

all_t_ranges= [t_seed_ranges]

for i in range(7):
    print(types[i]+" to "+types[i+1]+' conversion:')
    all_t_ranges.append([])
    for interval in all_t_ranges[i]:
        all_t_ranges[i+1].extend(determine_overlapping_ranges(interval, new_test_maps[i]))

min([x[0] for x in all_t_ranges[-1]])


all_big_ol_fuckin_ranges = [seed_ranges]

for i in range(7):
    print(types[i]+" to "+types[i+1]+' conversion:')
    all_big_ol_fuckin_ranges.append([])
    for interval in all_big_ol_fuckin_ranges[i]:
        print(interval)
        ranges_to_add = determine_overlapping_ranges(interval, all_them_new_maps[i])
        for x in ranges_to_add:
            if x[1] < x[0]:
                print(interval, x)
        all_big_ol_fuckin_ranges[i+1].extend(ranges_to_add)


min([x[0] for x in all_big_ol_fuckin_ranges[-1]])

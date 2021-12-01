import copy
with open("day13_input.txt", "r") as file:
    rows = file.readlines()

current_time = int(rows[0][:-1])
buses = rows[1][:-1].split(',')
test_buses = ['7','13','x','x','59','x','31','19']
bus_numbers = [int(bus) for bus in buses if bus != 'x']

times_when_theresa_bus = []
for bus_number in bus_numbers:
    for i in range(80000):
        times_when_theresa_bus.append([bus_number * i, bus_number])

times_when_theresa_bus.sort(key=lambda x: x[0])

valid_buses = []
for bus_time in times_when_theresa_bus:
    if bus_time[0] > current_time:
        valid_buses.append(bus_time)

valid_buses.sort(key=lambda x: x[0])
print((valid_buses[0][0]-current_time) * valid_buses[0][1])

# part 2

buses_to_check = [[int(bus), buses.index(bus)] for bus in buses if bus != 'x']
test_buses_to_check = [[int(bus), test_buses.index(bus)] for bus in test_buses if bus != 'x']

# n_i = buses_to_check[i][0]
# a_i = buses_to_check[i][1]
# there exists x such that for all i, x = (n_i - a_i) mod n_i
# find smallest x such that x + a_0 is divisible by n_0 (i.e. x = n_0 - a_0 mod n_0)
# this plus any multiple of n_0 will satisfy the i=0 equation
# find one that also satisfies x = n_1 - a_1 mod n_1
# this plus any multiple of n_0 * n_1 will satisfy the i=1 equation
# find one that also satisfied x = n_2 - a_2 mod n_2
# ...

x = (test_buses_to_check[0][0] - test_buses_to_check[0][1]) % test_buses_to_check[0][0]
running_product = 1
for i in range(1, len(test_buses_to_check)):
    print(x)
    running_product *= test_buses_to_check[i-1][0]
    while (test_buses_to_check[i][0] - test_buses_to_check[i][1]) % test_buses_to_check[i][0] != x % test_buses_to_check[i][0]:
        x += running_product
print(x)

x = (buses_to_check[0][0] - buses_to_check[0][1]) % buses_to_check[0][0]
running_product = 1
for i in range(1, len(buses_to_check)):
    print(x)
    running_product *= buses_to_check[i-1][0]
    while (buses_to_check[i][0] - buses_to_check[i][1]) % buses_to_check[i][0] != x % buses_to_check[i][0]:
        x += running_product
print(x)



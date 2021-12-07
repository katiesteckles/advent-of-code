import copy
with open("2021/day07_input.txt", "r") as file:
    input = file.readlines()

crab_pos = list(map(int, input[0].split(',')))

def find_fuel_cost(crab_pos, pos):
    cost = 0
    for crab in crab_pos:
        cost += abs(crab-pos)
    return cost

optimum = min(find_fuel_cost(crab_pos,i) for i in range(max(crab_pos)))
print(optimum)

# part 2
def find_fuel_cost2(crab_pos, pos):
    cost = 0
    for crab in crab_pos:
        distance = abs(crab-pos)
        cost += (distance*(distance+1))/2
    return cost

optimum2 = min(find_fuel_cost2(crab_pos,i) for i in range(max(crab_pos)))
print(int(optimum2))
with open("2022/day11_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]


def read_in_lines(monkey_facts):
    monkey_info = []
    for monkey in range(int((len(monkey_facts) + 1) / 7)):
        index = (monkey * 7)
        monkey_index = int(monkey_facts[index][monkey_facts[index].find(' ') + 1:monkey_facts[index].find(':')])
        index += 1
        monkey_items = (monkey_facts[index][monkey_facts[index].find(':') + 2:]).split(', ')
        index += 1
        monkey_operation = (monkey_facts[index][monkey_facts[index].find('old') + 4:]).split(' ')
        if monkey_operation == ['*','old']:
            monkey_operation = ['**','2']
        index += 1
        monkey_div = int(monkey_facts[index][monkey_facts[index].find('by') + 2:])
        index += 1
        monkey_iftrue = int(monkey_facts[index][monkey_facts[index].find('monkey') + 7:])
        index += 1
        monkey_iffalse = int(monkey_facts[index][monkey_facts[index].find('monkey') + 7:])
        monkey_info.append([monkey_index,monkey_items,monkey_operation,monkey_div,monkey_iftrue,monkey_iffalse,0])
    return monkey_info


monkey_info = read_in_lines(input)


# 0 monkey index; 1 list of items; 2 operation/value; 3 divisibility check; 4 if true; 5 if false; 6 item count

def monkey_time(monkey_info):
    for monkey in monkey_info:
        while len(monkey[1]) > 0:
            monkey[6] += 1
            current_item = monkey[1].pop(0)
            print(str(current_item) + ''.join(monkey[2]))
            current_item = eval(str(current_item) + ''.join(monkey[2]))
            current_item = int(current_item / 3)
            if current_item % monkey[3] == 0:
                monkey_info[monkey[4]][1].append(current_item)
            else:
                monkey_info[monkey[5]][1].append(current_item)


for i in range(20):
    monkey_time(monkey_info)

monkey_numbers = [monkey[6] for monkey in monkey_info]
monkey_numbers.sort()
print(monkey_numbers[-2:][0] * monkey_numbers[-2:][1])

# Part B

mega_monkey_modprod = 1
for monkey in monkey_info:
    mega_monkey_modprod *= monkey[3]


def modular_monkey_mambo(monkey_info):
    for monkey in monkey_info:
        while len(monkey[1]) > 0:
            monkey[6] += 1
            current_item = monkey[1].pop(0)
            # print(str(current_item) + ''.join(monkey[2]))
            current_item = eval(str(current_item) + ''.join(monkey[2]))
            current_item = current_item % mega_monkey_modprod
            if current_item % monkey[3] == 0:
                monkey_info[monkey[4]][1].append(current_item)
            else:
                monkey_info[monkey[5]][1].append(current_item)


for i in range(10000):
    modular_monkey_mambo(monkey_info)

monkey_numbers = [monkey[6] for monkey in monkey_info]
monkey_numbers.sort()
print(monkey_numbers[-2:][0] * monkey_numbers[-2:][1])

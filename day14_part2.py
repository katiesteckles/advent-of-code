import copy
with open("day14_input.txt", "r") as file:
    rows = file.readlines()

commands = [row[:-1] for row in rows]
commands_split = [[command[7:]] if command[:4] == 'mask' else command[4:].split('] = ') for command in commands]
test_commands_split = [['000000000000000000000000000000X1001X'], ['42','100'], ['00000000000000000000000000000000X0XX'], ['26','1']]

def interpret_bitmask(bitmask):
    proto_bitmask = 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'
    bitmask_list = []
    for i in range(36):
        if bitmask[i] == '0':
            splitmask = list(proto_bitmask)
            splitmask[i] = 'X'
            proto_bitmask = ''.join(splitmask)
        elif bitmask[i] == '1':
            splitmask = list(proto_bitmask)
            splitmask[i] = '1'
            proto_bitmask = ''.join(splitmask)
    number_of_Bs = proto_bitmask.count('B')
    bits_to_input_list = ['0'*(number_of_Bs - len(bin(i)[2:])) + bin(i)[2:] for i in range(2**number_of_Bs)]
    for j in range(2**number_of_Bs):
        current_proto_bitmask = copy.deepcopy(proto_bitmask)
        proto_splitmask = list(current_proto_bitmask)
        bits_replaced = 0
        for i in range(36):
            if proto_splitmask[i] == 'B':
                proto_splitmask[i] = bits_to_input_list[j][bits_replaced]
                bits_replaced += 1
        bitmask_list.append(''.join(proto_splitmask))
    return bitmask_list

# interpret_bitmask('000000000000000000000000000000X1001X')

data_slots = {}
current_bitmask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
for current_command in commands_split:
    if len(current_command) == 1: #it's a mask!
        # find all the bitmasks
        current_bitmasks = interpret_bitmask(current_command[0])
    elif len(current_command) == 2: # it's a memory assignment! change this so it applies the mask to the other one
        print(str(current_command) + ' is a memory assignment')
        # apply all possible bitmasks to the address you need to assign to and make a list
        locations_to_assign_to = []
        short_binary_string = bin(int(current_command[0]))[2:] # convert command[0] to binary
        binary_string = '0'*(36 - len(short_binary_string)) + short_binary_string
        # print('Need to assign ' + binary_string + ' to slot ' + str(current_command[0]))
        for i in range(len(current_bitmasks)):
            for j in range(36):
                if current_bitmasks[i][j] != 'X':
                    binary_string_list = list(binary_string)
                    binary_string_list[j] = current_bitmasks[i][j]
                    binary_string = ''.join(binary_string_list)
            number_to_assign_to = int(binary_string,2)
            data_slots[number_to_assign_to] = int(current_command[1])
print(data_slots)

total = sum(data_slots.values())
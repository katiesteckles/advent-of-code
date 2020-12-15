import copy
with open("day14_input.txt", "r") as file:
    rows = file.readlines()

commands = [row[:-1] for row in rows]
commands_split = [[command[7:]] if command[:4] == 'mask' else command[4:].split('] = ') for command in commands]
test_commands_split = [['XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'], ['8','11'], ['7','101'], ['8','0']]

data_slots = {}
current_bitmask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
for current_command in commands_split:
    print('Bitmask is ' + str(current_bitmask))
    if len(current_command) == 1: #it's a mask! set the bitmask
        print(str(current_command) + ' is a new bitmask')
        current_bitmask = current_command[0]
    elif len(current_command) == 2: # it's a memory assignment!
        print(str(current_command) + ' is a memory assignment')
        short_binary_string = bin(int(current_command[1]))[2:] # convert command[1] to binary
        binary_string = '0'*(36 - len(short_binary_string)) + short_binary_string
        print('Need to assign ' + binary_string + ' to slot ' + str(current_command[0]))
        for i in range(36):
            if current_bitmask[i] != 'X':
                binary_string_list = list(binary_string)
                binary_string_list[i] = current_bitmask[i]
                binary_string = ''.join(binary_string_list)
        print('After applying bitmask, it is ' + binary_string)
        number_to_assign = int(binary_string,2)
        data_slots[current_command[0]] = number_to_assign
print(data_slots)

total = sum(data_slots.values())

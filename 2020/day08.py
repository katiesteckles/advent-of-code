import copy

with open("day08_input.txt", "r") as file:
    commands = file.readlines()

commands = [command[:-1].split(' ') for command in commands]
commands = [[command[0], command[1][0], command[1][1:]] for command in commands]

def run_program(commands):
    running = 1
    total = 0
    current_line = 0
    print('Executing line ' + str(current_line))
    lines_used = []
    print('Lines used: '+ str(lines_used))
    while running == 1:
        if commands[current_line][0] == 'acc':
            if commands[current_line][1] == '+':
                total = total + int(commands[current_line][2])
            else:
                total = total - int(commands[current_line][2])
            lines_used.append(current_line)
            new_line = current_line + 1
            print('ACC ' + str(commands[current_line][1]) + str(commands[current_line][2]) + ': Total is now ' + str(
                total) + '; will now execute line ' + str(new_line))
        elif commands[current_line][0] == 'nop':
            lines_used.append(current_line)
            new_line = current_line + 1
            print('NOP; will now execute line ' + str(new_line))
        elif commands[current_line][0] == 'jmp':
            if commands[current_line][1] == '+':
                new_line = current_line + int(commands[current_line][2])
            else:
                new_line = current_line - int(commands[current_line][2])
            print('JMP ' + str(commands[current_line][1]) + str(commands[current_line][2]) + ': Will now execute line ' + str(new_line))
            lines_used.append(current_line)
        if new_line in lines_used:
            print('Line ' + str(new_line) + ' has been used twice, and the total is now ' + str(total) + '.')
            print('Lines used: ' + str(sorted(lines_used)))
            running = 0
        if new_line >= len(commands):
            print('Out of commands! Program terminated, and the total is now ' + str(total) + '.')
            running = 0
        current_line = new_line

def run_program_quietly(commands):
    running = 1
    total = 0
    current_line = 0
    #print('Executing line ' + str(current_line))
    lines_used = []
    #print('Lines used: '+ str(lines_used))
    while running == 1:
        if commands[current_line][0] == 'acc':
            if commands[current_line][1] == '+':
                total = total + int(commands[current_line][2])
            else:
                total = total - int(commands[current_line][2])
            lines_used.append(current_line)
            new_line = current_line + 1
            #print('ACC ' + str(commands[current_line][1]) + str(commands[current_line][2]) + ': Total is now ' + str(
            #    total) + '; will now execute line ' + str(new_line))
        elif commands[current_line][0] == 'nop':
            lines_used.append(current_line)
            new_line = current_line + 1
            #print('NOP; will now execute line ' + str(new_line))
        elif commands[current_line][0] == 'jmp':
            if commands[current_line][1] == '+':
                new_line = current_line + int(commands[current_line][2])
            else:
                new_line = current_line - int(commands[current_line][2])
            #print('JMP ' + str(commands[current_line][1]) + str(commands[current_line][2]) + ': Will now execute line ' + str(new_line))
            lines_used.append(current_line)
        if new_line in lines_used:
            #print('Line ' + str(new_line) + ' has been used twice, and the total is now ' + str(total) + '.')
            #print('Lines used: ' + str(sorted(lines_used)))
            running = 0
            return([total,'loop'])
        if new_line >= len(commands):
            #print('Out of commands! Program terminated, and the total is now ' + str(total) + '.')
            running = 0
            return([total,'term'])
        current_line = new_line

for i in range(len(commands)):
    testcommand = copy.deepcopy(commands)
    if testcommand[i][0] == 'jmp':
        print('Changing line ' + str(i) + '...')
        testcommand[i][0] = 'nop'
        if run_program_quietly(testcommand)[1] == 'term':
            print('Changing the ' + str(i)+'th line to nop will fix the program, and the total is '+ str(run_program_quietly(testcommand)[0]) + '.')
            break
with open("2025/day01.txt", "r") as file:
    input = file.readlines()
    input = [[line.strip()[0],int(line.strip()[1:])] for line in input]

def rotate_dial(current_value, turn_instruction):
    output_value = current_value
    if turn_instruction[0] == 'R':
        output_value += turn_instruction[1]
    elif turn_instruction[0] == 'L':
        output_value -= turn_instruction[1]
    output_value = output_value % 100
    return output_value

zero_count = 0
dial_value = 50
for turn_instruction in input:
    dial_value = rotate_dial(dial_value, turn_instruction)
    print(dial_value)
    if dial_value == 0:
        zero_count += 1

# Part 2


def step_rotate_dial(current_value, turn_instruction):
    steps = [current_value]
    output_value = current_value
    if turn_instruction[0] == 'R':
        for i in range(turn_instruction[1]):
            output_value += 1
            steps.append(output_value % 100)
    elif turn_instruction[0] == 'L':
        for i in range(turn_instruction[1]):
            output_value -= 1
            steps.append(output_value % 100)
    output_value = output_value % 100
    return [output_value, steps[:-1]]

zero_pass_count = 0
dial_value = 50
steps = []
for turn_instruction in input:
    [dial_value, new_steps] = step_rotate_dial(dial_value, turn_instruction)
    print(dial_value)
    print(new_steps)
    steps.extend(new_steps)
zero_pass_count = steps.count(0)


with open("day05_input.txt", "r") as file:
    data = file.readlines()

passes = [x[:-1] for x in data]

to_add = [[0,64],[0,32],[0,16],[0,8],[0,4],[0,2],[0,1]]

def string_to_num(string):
    number = 0
    for i in range(len(string)):
        if string[-(i+1)] == 'F' or string[-(i+1)] == 'L':
            number += to_add[-(i+1)][0]
        else:
            number += to_add[-(i+1)][1]
    return number

def seat_id(string):
    row = string_to_num(string[:7])
    col = string_to_num(string[7:])
    return (row * 8) + col

seat_ids = [seat_id(board_pass) for board_pass in passes]

for x in seat_ids:
    if x-2 in seat_ids and x-1 not in seat_ids:
        print(str(x-2) + ', ' + str(x-1) + ' (you), ' + str(x))

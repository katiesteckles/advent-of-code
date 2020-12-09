import copy
with open("day09_input.txt", "r") as file:
    numbers = file.readlines()

numbers = [int(number[:-1]) for number in numbers[:-1]]
window_length= 25

# check the 26th number to see if it can be made from two of the numbers between the 1st and 25th number
# check the 27th number to see if it can be made from two of the numbers between the 2nd and 26th number
# check the 28th number to see if it can be made from two of the numbers between the 3rd and 27th number

for aim_sum_index in range(window_length+1, len(numbers)):
    aim_sum = numbers[aim_sum_index]
    print('Total needed: ' + str(aim_sum))
    found_it = 0
    for j in range(window_length):
        for k in range(j, window_length):
            # print('Trying ' + str(numbers[aim_sum_index-window_length+j]) + ' + ' + str(numbers[aim_sum_index-window_length+k]) + '...')
            if numbers[aim_sum_index - window_length + j] + numbers[aim_sum_index - window_length + k] == aim_sum:
                print(str(numbers[aim_sum_index - window_length + j]) + ' + ' + str(
                    numbers[aim_sum_index - window_length + k]) + ' = ' + str(aim_sum))
                found_it = 1
    if found_it == 0:
        print('No two numbers could be found within numbers ' + str(aim_sum_index - window_length) + ' to ' + str(aim_sum_index) + ' which sum to ' + str(aim_sum) + '.')
        break

number_to_find = 1639024365

breakable_numbers = copy.deepcopy(numbers)
got_it = 0
while got_it == 0:
    for i in range(len(breakable_numbers)):
        if sum(breakable_numbers[:i]) == number_to_find:
            print('The sum of the numbers between ' + str(breakable_numbers[0]) + ' and ' + str(breakable_numbers[i]) + ' is ' + str(number_to_find) + '.')
            endpoints = [breakable_numbers[0], breakable_numbers[i]]
            got_it = 1
        elif sum(breakable_numbers[:i]) > number_to_find:
            break
    breakable_numbers = breakable_numbers[1:]

max(numbers[numbers.index(endpoints[0]):numbers.index(endpoints[1])]) + min(numbers[numbers.index(endpoints[0]):numbers.index(endpoints[1])])
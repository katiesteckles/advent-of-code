import copy
with open("2021/day03_input.txt", "r") as file:
    numbers = file.readlines()

numbers = [list(x[:-1]) for x in numbers]

# part 1

gamma = list('0'*len(numbers[0]))
for i in range(len(numbers[0])):
    sumi = 0
    for number in numbers:
        sumi += int(number[i])
    if sumi > 500:
        gamma[i]='1'

gammanum = int(''.join(gamma),2)
epsilonnum = 4095 - gammanum
print(epsilonnum * gammanum)

# part 2
numbers_id = copy.deepcopy(numbers)
for i in range(len(numbers_id)):
    numbers_id[i].append(i)

def check_and_chop(numbers_id, digit):
    total = sum([int(number[digit]) for number in numbers_id])
    digpos = len(numbers[0]) - len(numbers_id[0])+1
    if total >= len(numbers_id)/2:
        print('The most popular value for digit '+ str(digpos) +' is 1')
        new_list = [number[1:] for number in numbers_id if number[0] == '1']
    else:
        print('The most popular value for digit ' + str(digpos) + ' is 0')
        new_list = [number[1:] for number in numbers_id if number[0] == '0']
    return new_list

def check_and_chop_co2(numbers_id, digit):
    total = sum([int(number[digit]) for number in numbers_id])
    digpos = len(numbers[0]) - len(numbers_id[0])+1
    if total < len(numbers_id)/2:
        print('The least popular value for digit '+ str(digpos) +' is 1')
        new_list = [number[1:] for number in numbers_id if number[0] == '1']
    else:
        print('The least popular value for digit ' + str(digpos) + ' is 0')
        new_list = [number[1:] for number in numbers_id if number[0] == '0']
    return new_list

sets = []
sets.append(check_and_chop(numbers_id,0))
for i in range(len(numbers[0])-1):
    sets.append(check_and_chop(sets[-1],0))

oxgen = numbers_id[sets[-1][0][0]]

sets_co2 = []
sets_co2.append(check_and_chop_co2(numbers_id,0))
for i in range(len(numbers[0])-1):
    sets_co2.append(check_and_chop_co2(sets_co2[-1],0))

co2gen = numbers_id[sets_co2[-2][0][-1]]

oxnum = int(''.join(oxgen[:-1]),2)
co2num = int(''.join(co2gen[:-1]),2)

print(oxnum*co2num)
with open("day1_input.txt", "r") as file:
    numbers = file.readlines()

numbers_int = [int(x[:-1]) for x in numbers]

# Two numbers that add to 2020
for i in range(len(numbers_int)):
    for j in range(i, len(numbers_int)):
        # print('Testing ' + str(numbers_int[i]) + ' and ' + str(numbers_int[j]) + '...')
        if numbers_int[i]+numbers_int[j]==2020:
            print(str(numbers_int[i]) + ' + ' + str(numbers_int[j]) + ' = 2020; The product is ' + str(numbers_int[i]*numbers_int[j]))

# Three numbers that add to 2020
for i in range(len(numbers_int)):
    for j in range(i, len(numbers_int)):
        for k in range(j, len(numbers_int)):
            if numbers_int[i]+numbers_int[j]+numbers_int[k]==2020:
                print(str(numbers_int[i]) + ' + ' + str(numbers_int[j]) + ' + ' + str(numbers_int[k]) + ' = 2020; The product is ' + str(numbers_int[i]*numbers_int[j]*numbers_int[k]))



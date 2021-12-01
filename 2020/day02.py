with open("day02_input.txt", "r") as file:
    passwords = file.readlines()

passwords_split = [[x[0].split("-")[0],x[0].split("-")[1].split(" ")[0],x[0].split("-")[1].split(" ")[1],x[1][:-1]] for x in [y.split(": ") for y in passwords]]

# part 1
countervariable = 0
for i in range(len(passwords_split)):
    if passwords_split[i][3].count(passwords_split[i][2]) >= int(passwords_split[i][0]) and passwords_split[i][3].count(passwords_split[i][2]) <= int(passwords_split[i][1]):
        print('The string ' + passwords_split[i][3] + ' contains ' + str(passwords_split[i][3].count(passwords_split[i][2])) + ' ' + passwords_split[i][2] + 's, which is between ' + passwords_split[i][0] + ' and ' + passwords_split[i][1] + '.')
        countervariable += 1
print('There were a total of ' + str(countervariable) + ' valid passwords.')

# part 2
countervariable_2 = 0
for i in range(len(passwords_split)):
    first_num = int(passwords_split[i][0])
    second_num = int(passwords_split[i][1])
    letter_of_note = passwords_split[i][2]
    password_to_check = passwords_split[i][3]
    if password_to_check[first_num-1] == letter_of_note:
        print('Letter ' + str(first_num) + ' in ' + password_to_check + ' is ' + letter_of_note + ', as required.')
        if password_to_check[second_num-1] == letter_of_note:
            print('Letter ' + str(second_num) + ' in ' + password_to_check + ' is also ' + letter_of_note + ', which means it fails.')
        else:
            print('Letter ' + str(second_num) + ' in ' + password_to_check + ' is not ' + letter_of_note + ', which means it passes!')
            countervariable_2 += 1
    else:
        print('Letter ' + str(first_num) + ' in ' + password_to_check + ' is not ' + letter_of_note + '.')
        if password_to_check[second_num-1] == letter_of_note:
            print('But letter ' + str(second_num) + ' in ' + password_to_check + ' is ' + letter_of_note + ', so it passes!')
            countervariable_2 += 1
        else:
            print('And ' + str(second_num) + ' in ' + password_to_check + ' is not ' + letter_of_note + ' either, so it fails.')
print('There were a total of ' + str(countervariable_2) + ' valid passwords.')

with open("2025/day03.txt", "r") as file:
    input = file.readlines()
    input = [line[:-1] for line in input]


testinput = ['987654321111111','811111111111119','234234234234278','818181911112111']

def find_largest_digit(numstring):  # returns: largest digit, zero-indexed position of largest digit
    for i in range(9,0,-1):
        if numstring.find(str(i)) >= 0:
            return [i, numstring.find(str(i))]

total = 0
for line in input:
    first_digit = find_largest_digit(line)
    if int(first_digit[1])+1 == len(line):
        second_digit = first_digit
        first_digit = find_largest_digit(line[:-1])
    else:
        second_digit = find_largest_digit(line[int(first_digit[1])+1:])
    print(first_digit,second_digit)
    number = int(first_digit[0])*10 + int(second_digit[0])
    total += number

# Part B
twelvetotal = 0
for line in input:
    theline = line
    n = 11
    digits = []
    while n > 0:
        digits.append(find_largest_digit(theline[:-n]))
        theline = theline[digits[-1][1]+1:]
        print(n, digits, theline)
        n -= 1
    digits.append(find_largest_digit(theline))
    print('0', digits, theline)
    number = 0
    for digit in digits:
        number += int(digit[0])
        number *= 10
    number = number // 10 # haaaaaaaaack
    print(str(number))
    twelvetotal += number

twelvetotal




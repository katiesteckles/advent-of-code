with open("2023/day01_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

test_input = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
digits = "0123456789"


def extract_numbers(list):
    total = 0
    for item in list:
        numbers = []
        for letter in [*item]:
            if letter in digits:
                numbers.append(int(letter))
        total += (10 * numbers[0]) + numbers[-1]
    return total


extract_numbers(test_input)

extract_numbers(input)

# Part B

test_input_b = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

digits_verbose = {"one": 1,
                  "two": 2,
                  "three": 3,
                  "four": 4,
                  "five": 5,
                  "six": 6,
                  "seven": 7,
                  "eight": 8,
                  "nine": 9}


def extract_numbers_verbose(list):
    total = 0
    for item in list:
        print("Item: " + item)
        i = 1
        numbers = []
        while len(item) > 0:
            # treat the case where you're on the last character
            if len(item) == 1:
                if item in digits:
                    numbers.append(item)
                break
            # create a window that expands until it finds something
            chunk = item[0:i]
            if chunk in digits:  # found a single-digit number
                numbers.append(int(chunk))
                item = item[1:]
            elif chunk in digits_verbose:  # found a word number
                numbers.append(digits_verbose[chunk])
                item = item[1:]
                i = 1
            elif i > 5:  # defo doesn't start with a number at all so take off the first character
                item = item[1:]
                i = 1
            else:  # didn't find either so just look for longer words
                i += 1
        print(numbers)
        total += (10 * numbers[0]) + numbers[-1]
    return total


extract_numbers_verbose(test_input_b)

extract_numbers_verbose(input)
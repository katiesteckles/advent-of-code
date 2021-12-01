with open("day01_input.txt", "r") as file:
    numbers = file.readlines()

numbers_int = [int(x[:-1]) for x in numbers]

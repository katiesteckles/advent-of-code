with open("2023/day02_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

test_input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

colours = ['red', 'green', 'blue']
digits = "0123456789"

def parse_input(listofgames):
    all_games = []
    for game in listofgames:
        gamedraws = []
        game = [game[5:game.find(':')],game[(game.find(':')+1):].split(';')]
        for draw in game[1]:
            draw_s = draw.strip()
            i = 1
            cubes_drawn = [[],[],[]] # red, green, blue
            value = ''
            while len(draw_s)>3:
                # create a window that expands until it finds something
                chunk = draw_s[0:i]
                if chunk in digits:  # found a digit
                    value = value+chunk
                    draw_s = draw_s[1:]
                elif chunk == ',':  # found a comma
                    draw_s = draw_s[1:]
                elif chunk == ' ':  # found a space
                    draw_s = draw_s[1:]
                    if draw_s[0] == 'r':
                        cubes_drawn[0] = int(value)
                        value = ''
                        draw_s = draw_s[3:]
                    elif draw_s[0] == 'g':
                        cubes_drawn[1] = int(value)
                        value = ''
                        draw_s = draw_s[5:]
                    elif draw_s[0] == 'b':
                        cubes_drawn[2] = int(value)
                        value = ''
                        draw_s = draw_s[4:]
            for i in range(3):
                if not cubes_drawn[i]:
                    cubes_drawn[i] = 0
            gamedraws.append(cubes_drawn)
        all_games.append(gamedraws)
    return all_games

test_better = parse_input(test_input)

input_better = parse_input(input)

maxes = [12, 13, 14]

def valid_game(game):
    for draw in game:
        for i in range(3):
            #if not draw[i]:
            #    draw[i] = 0
            if draw[i] > maxes[i]:
                return False
    return True

total_test = 0
for n in range(len(test_better)):
    if valid_game(test_better[n]):
        total_test += n+1


total = 0
for n in range(len(input_better)):
    if valid_game(input_better[n]):
        total += n+1


# Part 2

import math as maths

def find_power(game):
    maxcols = [0,0,0]
    for draw in game:
        for i in range(3):
            print(maxcols, game)
            maxcols[i] = max([maxcols[i], draw[i]])
    return maths.prod(maxcols)


test_powertotal = 0
powertotal = 0

for game in test_better:
    test_powertotal += find_power(game)

for game in input_better:
    powertotal += find_power(game)

with open("2022/day02_input.txt","r") as file:
    input = file.readlines()
    input = [item[0] + item[-2] for item in input]

testinput = ["AY","BX","CZ"]

# AX Rock BY Paper CZ Scissors
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus (0 if you lost, 3 if the round was a draw, and 6 if you won).

letter_names = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

base_scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

winning = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}


def calculate_score(game):
    score = 0
    score += base_scores[letter_names[game[1]]]
    if letter_names[game[0]] == letter_names[game[1]]:
        score += 3
        return score
    elif winning[letter_names[game[0]]] == letter_names[game[1]]:
        return score
    elif winning[letter_names[game[1]]] == letter_names[game[0]]:
        score += 6
        return score


calculate_score("BX")

scoring_dict_gen = {}

theirmoves = ["A", "B", "C"]
mymoves = ["X", "Y", "Z"]

for i in range(len(theirmoves)):
    for j in range(len(mymoves)):
        scoring_dict_gen[theirmoves[i] + mymoves[j]] = calculate_score(theirmoves[i] + mymoves[j])

score = 0
for game in input:
    score += scoring_dict_gen[game]

print(score)

# Part B

#  X lose, Y draw, and Z win.

what_i_do = {
    "AX": "C",
    "AY": "A",
    "AZ": "B",
    "BX": "A",
    "BY": "B",
    "BZ": "C",
    "CX": "B",
    "CY": "C",
    "CZ": "A"
}

def calculate_score_B(game):
    score = 0
    game = game[0]+what_i_do[game]
    score += base_scores[letter_names[game[1]]]
    if letter_names[game[0]] == letter_names[game[1]]:
        score += 3
        return score
    elif winning[letter_names[game[0]]] == letter_names[game[1]]:
        return score
    elif winning[letter_names[game[1]]] == letter_names[game[0]]:
        score += 6
        return score

score = 0
for game in input:
    score += calculate_score_B(game)

print(score)
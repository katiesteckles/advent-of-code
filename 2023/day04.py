with open("2023/day04_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]


# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

cards = [[line[9:].split(' | ')[0].strip().split(' '),line[9:].split(' | ')[1].strip().split(' ')] for line in input]
cards = [[[int(nummo) for nummo in card[0] if nummo != ''],[int(nummo) for nummo in card[1] if nummo != '']] for card in cards]

def calculate_score(cards):
    score = 0
    for card in cards:
        winno = 0
        for nummo in card[1]:
            if nummo in card[0]: winno += 1
        if winno > 0: score += 2 ** (winno - 1)
    return score


calculate_score(cards)

calculate_score([cards[0]])

# Part 2

card_counts = [1]*len(cards)

def calculate_matches(card):
    winno = 0
    for nummo in card[1]:
        if nummo in card[0]: winno += 1
    return winno

for i in range(len(cards)):
    print(i)
    for j in range(calculate_matches(cards[i])):
        card_counts[i+j+1] += card_counts[i]

sum(card_counts)

with open("2023/day07_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip().split(' ') for line in input]

hand_types = {
    'high': 0,
    'pair': 1,
    'twopair': 2,
    'three': 3,
    'full': 4,
    'four': 5,
    'five': 6
}

card_ranks = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}


def hand_type(hand):
    if len(set(hand)) == 1:
        return 'five'
    elif len(set(hand)) == 2:
        counts = []
        for card in set(hand):
            counts.append(hand.count(card))
        counts.sort()
        if counts == [1, 4]:
            return 'four'
        elif counts == [2, 3]:
            return 'full'
    elif len(set(hand)) == 3:
        counts = []
        for card in set(hand):
            counts.append(hand.count(card))
        counts.sort()
        if counts == [1, 1, 3]:
            return 'three'
        if counts == [1, 2, 2]:
            return 'twopair'
    elif len(set(hand)) == 4:
        return 'pair'
    elif len(set(hand)) == 5:
        return 'high'


def compare_cards(hand1, hand2):  # takes in two five-character strings
    if hand_types[hand_type(hand1)] > hand_types[hand_type(hand2)]:
        return hand1
    elif hand_types[hand_type(hand1)] < hand_types[hand_type(hand2)]:
        return hand2
    elif hand_types[hand_type(hand1)] == hand_types[hand_type(hand2)]:
        for i in range(5):
            if card_ranks[hand1[i]] > card_ranks[hand2[i]]:
                return hand1
            elif card_ranks[hand1[i]] < card_ranks[hand2[i]]:
                return hand2


import copy

test_input = [['32T3K', '765'], ['T55J5', '684'], ['KK677', '28'], ['KTJJT', '220'], ['QQQJA', '483']]

cards_list = copy.deepcopy(input)
nochange = 0
runthrough = 0
while nochange == 0:
    runthrough += 1
    print('Round ' + str(runthrough))
    newlist = copy.deepcopy(cards_list)
    for i in range(len(cards_list) - 1):
        print('Comparing cards ' + str(i) + ' and ' + str(i + 1) + '...')
        if compare_cards(newlist[i][0], newlist[i + 1][0]) == newlist[i][0]:
            print('Swapping!')
            temp = newlist[i]
            newlist[i] = newlist[i + 1]
            newlist[i + 1] = temp
    if newlist == cards_list:
        nochange = 1
    else:
        cards_list = newlist

total_score = 0
for i in range(len(cards_list)):
    total_score += (i + 1) * int(cards_list[i][1])

print(total_score)

# PART 2

jard_ranks = {
    'J': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

counts_dict = {
    (1, 4): 'four',
    (2, 3): 'full',
    (5,): 'five',
    (1, 4): 'four',
    (2, 3): 'full',
    (1, 1, 3): 'three',
    (1, 2, 2): 'twopair',
    (1, 1, 1, 2): 'pair',
    (1, 1, 1, 1, 1): 'high'
}


def jand_type(hand):
    if len(set(hand)) == 1:
        return 'five'
    else:
        jokers = hand.count('J')
        counts = []
        for card in set(hand):
            if card != 'J':
                counts.append(hand.count(card))
        counts.sort()
        counts[-1] += jokers
        return counts_dict[tuple(counts)]


def jompare_cards(hand1, hand2):  # takes in two five-character strings
    if hand_types[jand_type(hand1)] > hand_types[jand_type(hand2)]:
        return hand1
    elif hand_types[jand_type(hand1)] < hand_types[jand_type(hand2)]:
        return hand2
    elif hand_types[jand_type(hand1)] == hand_types[jand_type(hand2)]:
        for i in range(5):
            if jard_ranks[hand1[i]] > jard_ranks[hand2[i]]:
                return hand1
            elif jard_ranks[hand1[i]] < jard_ranks[hand2[i]]:
                return hand2


cards_list = copy.deepcopy(input)
nochange = 0
runthrough = 0
while nochange == 0:
    runthrough += 1
    print('Round ' + str(runthrough))
    newlist = copy.deepcopy(cards_list)
    for i in range(len(cards_list) - 1):
        print('Jomparing cards ' + str(i) + ' and ' + str(i + 1) + '...')
        if jompare_cards(newlist[i][0], newlist[i + 1][0]) == newlist[i][0]:
            print('Swapping!')
            temp = newlist[i]
            newlist[i] = newlist[i + 1]
            newlist[i + 1] = temp
    if newlist == cards_list:
        nochange = 1
    else:
        cards_list = newlist

jotal_score = 0
for i in range(len(cards_list)):
    jotal_score += (i + 1) * int(cards_list[i][1])

print(jotal_score)

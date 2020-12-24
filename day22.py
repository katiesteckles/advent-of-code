import copy
import re
with open("day22_input.txt", "r") as file:
    cards = file.readlines()

cards = [card[:-1] for card in cards]
hands = [cards[1:cards.index('Player 2:')-1], cards[cards.index('Player 2:')+1:]]

def play_a_round(hand1,hand2):
    print('Player 1 has ' + str(hand1))
    print('Player 2 has ' + str(hand2))
    print(str(hand1[0]) + ' vs ' + str(hand2[0]) + ':')
    if int(hand1[0]) > int(hand2[0]):
        print('Player 1 wins!')
        winning_card = hand1.pop(0)
        hand1.append(winning_card)
        losing_card = hand2.pop(0)
        hand1.append(losing_card)
    else:
        print('Player 2 wins!')
        winning_card = hand2.pop(0)
        hand2.append(winning_card)
        losing_card = hand1.pop(0)
        hand2.append(losing_card)

def quietly_play_a_round(hand1,hand2):
    if int(hand1[0]) > int(hand2[0]):
        print('Player 1 wins the regular game!')
        winning_card = hand1.pop(0)
        hand1.append(winning_card)
        losing_card = hand2.pop(0)
        hand1.append(losing_card)
    else:
        print('Player 2 wins the regular game!')
        winning_card = hand2.pop(0)
        hand2.append(winning_card)
        losing_card = hand1.pop(0)
        hand2.append(losing_card)

def calculate_score(hand):
    total = 0
    for i in range(len(hand)):
        total += int(hand[i]) * (len(hand)-i)
    return total

hand1 = copy.deepcopy(hands[0])
hand2 = copy.deepcopy(hands[1])
#hand1 = ['9','2','6','3','1']
#hand2 = ['5','8','4','7','10']
round_number = 1
while len(hand1) > 0 and len(hand2) > 0:
    print('Round ' + str(round_number))
    play_a_round(hand1, hand2)
    round_number += 1
print('Player 1 has ' + str(hand1) + '; Player 2 has ' + str(hand2))
print('Final scores: Player 1 = ' + str(calculate_score(hand1)) + '; Player 2 = ' + str(calculate_score(hand2)))

# part 2

def recursive_game(hand1,hand2):
    previous_hands1 = []
    previous_hands2 = []
    while len(hand1) > 0 and len(hand2) > 0:
        if hand1 not in previous_hands1 and hand2 not in previous_hands2:
            previous_hands1.append(copy.deepcopy(hand1))
            previous_hands2.append(copy.deepcopy(hand2))
            print('Player 1 has ' + str(len(hand1)) + ' cards: ' + str(hand1))
            print('Player 2 has ' + str(len(hand2)) + ' cards: ' + str(hand2))
            if (len(hand1)-1) >= int(hand1[0]) and (len(hand2)-1) >= int(hand2[0]):
                print('Initiating recursive game using hands of size ' + hand1[0] + ' and ' + hand2[0])
                card1 = hand1.pop(0)
                card2 = hand2.pop(0)
                if recursive_game(hand1[:int(card1)],hand2[:int(card2)]) == 1:
                    hand1.append(card1)
                    hand1.append(card2)
                else:
                    hand2.append(card2)
                    hand2.append(card1)
            else:
                print('Not enough cards for recursion... initiating regular game')
                quietly_play_a_round(hand1,hand2)
        else:
            print('This is a repeat hand! One of ' + str(hand1) + ' or ' + str(hand2) + ' has been seen before. Player 1 wins!')
            return 1
    print('Player 1 has ' + str(hand1) + '; Player 2 has ' + str(hand2))
    if len(hand1) == 0:
        print('Player 2 wins because the other player ran out of cards!')
        return 2
    elif len(hand2) == 0:
        print('Player 1 wins because the other player ran out of cards!')
        return 1

hand1 = copy.deepcopy(hands[0])
hand2 = copy.deepcopy(hands[1])
#hand1 = ['9', '2', '6', '3', '1']
#hand2 = ['5', '8', '4', '7', '10']
#hand1 = ['43', '19']
#hand2 = ['2', '29', '14']

recursive_game(hand1,hand2)
print('Final scores: Player 1 = ' + str(calculate_score(hand1)) + '; Player 2 = ' + str(calculate_score(hand2)))


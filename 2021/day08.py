import copy
with open("2021/day08_input.txt", "r") as file:
    input = file.readlines()
    input = [line[:-1] for line in input]

sets_sample = [[set(word) for word in line.split(' ')][:-5] for line in input]
sets_digits = [[set(word) for word in line.split(' ')][-4:] for line in input]

def find_uniques(digit_sets, length):
    no_uniques = 0
    for digit_set in digit_sets:
        for digit in digit_set:
            if len(digit) == length:
                no_uniques +=1
    return no_uniques

print(find_uniques(sets_digits,2)+find_uniques(sets_digits,3)+find_uniques(sets_digits,4)+find_uniques(sets_digits,7))

# part 2

def determine_digits(digit_set):
    digit_assignments = {}
    # identify 1 (2 segs), 4 (4 segs), 7 (3 segs), 8 (7 segs)
    for digit in digit_set:
        if len(digit) == 2:
            digit_assignments[1] = digit
            #print('1: ' + str(digit_assignments[1]))
        elif len(digit) == 3:
            digit_assignments[7] = digit
            #print('7: ' + str(digit_assignments[7]))
        elif len(digit) == 4:
            digit_assignments[4] = digit
            #print('4: ' + str(digit_assignments[4]))
        elif len(digit) == 7:
            digit_assignments[8] = digit
            #print('8: ' + str(digit_assignments[8]))
    # identify which three are missing from the 6s
    not_used_in_six_segs = set()
    fivesegs = [digit for digit in digit_set if len(digit) == 5]
    sixsegs = [digit for digit in digit_set if len(digit) == 6]
    for sixseg in sixsegs:
        not_used_in_six_segs |= digit_assignments[8]-sixseg
    #print('Not used in six-segment digits: '+str(not_used_in_six_segs))
    # 2 = the only five-seg that contains all three
    digit_assignments[2] = [digit for digit in fivesegs if len(digit & not_used_in_six_segs) == 3][0]
    #print('2: '+str(digit_assignments[2]))
    # 5 = the five-seg that contains exactly one of those three
    digit_assignments[5] = [digit for digit in fivesegs if len(digit & not_used_in_six_segs) == 1][0]
    #print('5: ' + str(digit_assignments[5]))
    # 3 = the remaining 5-seg
    for fiveseg in fivesegs:
        if fiveseg != digit_assignments[2] and fiveseg != digit_assignments[5]:
            digit_assignments[3] = fiveseg
            #print('3: ' + str(digit_assignments[3]))
    # identify which single seg is common to 2, 4 & 5
    central_seg = digit_assignments[2] & digit_assignments[4] & digit_assignments[5]
    #print('Central segment: '+str(central_seg))
    # 0 = the six-seg missing only that one
    for sixseg in sixsegs:
        if len(central_seg & sixseg) == 0:
            digit_assignments[0] = sixseg
            #print('0: ' + str(digit_assignments[0]))
    for sixseg in sixsegs:
        # 6 = the one of the two remaining that only shares one seg with 1
        if len(sixseg & digit_assignments[1]) == 1 and sixseg != digit_assignments[0]:
            digit_assignments[6] = sixseg
            #print('6: ' + str(digit_assignments[6]))
    for sixseg in sixsegs:
        # 9 = the other one
        if sixseg != digit_assignments[0] and sixseg != digit_assignments[6]:
            digit_assignments[9] = sixseg
            #print('9: ' + str(digit_assignments[9]))
    return digit_assignments

def decode_number(digit_set, sample_set):
    answer = ''
    digit_assignments = determine_digits(sample_set)
    for digit in digit_set:
        for j in range(len(digit_assignments)):
            if digit == digit_assignments[j]:
                answer += str(j)
    print(answer)
    return int(answer)

total = 0
for i in range(len(sets_digits)):
    total += decode_number(sets_digits[i], sets_sample[i])

print(total)
import string

with open("day06_input.txt", "r") as file:
    answers = file.readlines()

answers = [x[:-1] for x in answers]

line = 0
group_answers = []
for entry in answers:
    if entry == '':
        line += 1
    else:
        if len(group_answers) < line+1:
            group_answers.append([entry])
        else:
            group_answers[line].append(entry)

group_answers_sets = [set(''.join(x)) for x in group_answers]

#answer to part 1
sum(len(x) for x in group_answers_sets)

setty_group_answers = [set(x) for x in group_answers]

#answer to part 2
total = 0
for group in setty_group_answers:
    common_elts = set(string.ascii_lowercase)
    for item in group:
        common_elts = common_elts.intersection(set(item))
    total += len(common_elts)


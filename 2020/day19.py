import copy
import re
with open("day19_input.txt", "r") as file:
    lines = file.readlines()

number_lines = [line[:-1].replace('"','').split(': ') for line in lines if len(line[:-1]) > 0 and line[0] != 'a' and line[0] != 'b']
number_lines.sort(key=lambda x:int(x[0]))
pattern_lines = [line[:-1] for line in lines if len(line[:-1]) > 0 and (line[0] == 'a' or line[0] == 'b')]

ab_regex = re.compile('^[\\(\\)ab\\s\\|]*$')
lettery_rules = []

def find_lettery_rules(rule_list, l_rules):
    lr_to_add = [rule for rule in rule_list if ab_regex.match(rule[1])]
    for item in lr_to_add:
        if item not in l_rules:
            l_rules += [item]
    return l_rules

its_all_letters = 0
while its_all_letters == 0:
    lettery_rules = find_lettery_rules(number_lines, lettery_rules)
    print(len(lettery_rules))
    for rule in lettery_rules:
        for line in number_lines:
            str_to_find = re.compile('(^|\\s|\\()'+ rule[0] + '(\\)|\\s|$)')
            for i in range(2):
                line[1] = str_to_find.sub(' ( ' + rule[1] + ' ) ',line[1])
    if all(ab_regex.match(ln[1]) for ln in number_lines):
        its_all_letters = 1

# str_to_find = re.compile('(^|\\s)64(\\s|$)')
# str_to_find.sub(' FOO ',number_lines[7][1])

rule_0 = number_lines[0][1].replace(' ', '')

rule0_regex = re.compile('^'+ rule_0 + '$')
total = 0
for pattern in pattern_lines:
    if rule0_regex.match(pattern):
        total +=1
        print(total)

# part 2

import copy
import re

level_of_ridiculousness = 15

new8 = '42 '
for i in range(2,level_of_ridiculousness):
    new8 = new8 + '| ' + '42 '*i

new11 = '42 31 '
for i in range(2,level_of_ridiculousness):
    new11 = new11 + '| ' + '42 '*i + '31 '*i


with open("day19_input.txt", "r") as file:
    lines = file.readlines()

number_lines = [line[:-1].replace('"','').split(': ') for line in lines if len(line[:-1]) > 0 and line[0] != 'a' and line[0] != 'b']
number_lines.sort(key=lambda x:int(x[0]))
pattern_lines = [line[:-1] for line in lines if len(line[:-1]) > 0 and (line[0] == 'a' or line[0] == 'b')]

number_lines[8][1] = new8
number_lines[11][1] = new11

ab_regex = re.compile('^[\\(\\)ab\\s\\|]*$')
lettery_rules = []

def find_lettery_rules(rule_list, l_rules):
    lr_to_add = [rule for rule in rule_list if ab_regex.match(rule[1])]
    for item in lr_to_add:
        if item not in l_rules:
            l_rules += [item]
    return l_rules

its_all_letters = 0
while its_all_letters == 0:
    lettery_rules = find_lettery_rules(number_lines, lettery_rules)
    print(len(lettery_rules))
    for rule in lettery_rules:
        for line in number_lines:
            str_to_find = re.compile('(^|\\s|\\()'+ rule[0] + '(\\)|\\s|$)')
            for i in range(2):
                line[1] = str_to_find.sub(' ( ' + rule[1] + ' ) ',line[1])
    if all(ab_regex.match(ln[1]) for ln in number_lines):
        its_all_letters = 1

# str_to_find = re.compile('(^|\\s)64(\\s|$)')
# str_to_find.sub(' FOO ',number_lines[7][1])

rule_0 = number_lines[0][1].replace(' ', '')
print(rule_0)
print(len(rule_0))

rule0_regex = re.compile('^'+ rule_0 + '$')
total = 0
for pattern in pattern_lines:
    if rule0_regex.match(pattern):
        total +=1
        print(total)
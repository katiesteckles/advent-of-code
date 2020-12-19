import copy
import re
with open("day19_input.txt", "r") as file:
    lines = file.readlines()

number_lines = [line[:-1].replace('"','').split(': ') for line in lines if len(line[:-1]) > 0 and line[0] != 'a' and line[0] != 'b']
number_lines.sort(key=lambda x:int(x[0]))
pattern_lines = [line[:-1] for line in lines if len(line[:-1]) > 0 and (line[0] == 'a' or line[0] == 'b')]

dicto = dict(number_lines)

found_rule_0 = 0
while found_rule_0 = 0:
    


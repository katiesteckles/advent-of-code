import copy
with open("day16_input.txt", "r") as file:
    data = file.readlines()

data = [data_point.split(': ') for data_point in data]

for i in range(20):
    data[i][1] = data[i][1].split(' or ')

for i in range(20):
    data[i][1][0] = data[i][1][0].split('-')
    data[i][1][1] = data[i][1][1][:-1].split('-')

for i in range(20):
    low_1 = int(data[i][1][0][0])
    up_1 = int(data[i][1][0][1]) + 1
    low_2 = int(data[i][1][1][0])
    up_2 = int(data[i][1][1][1]) + 1
    data[i][1] = list(range(low_1, up_1)) + list(range(low_2, up_2))

rules = data[:20]

my_ticket = data[22][0][:-1].split(',')
my_ticket = [int(nmbr) for nmbr in my_ticket]

other_tickets = data[25:]
other_tickets = [ticket[0][:-1].split(',') for ticket in other_tickets]
int_other_tickets = []
for ticket in other_tickets:
    int_other_tickets.append([int(tick_num) for tick_num in ticket])

valid_numbers = set()
for i in range(len(rules)):
    for rule in rules[i][1]:
        valid_numbers.add(rule)

invalid_values = []
for ticket in int_other_tickets:
    for number in ticket:
        if number not in valid_numbers:
            print('We gotta live one here! Adding ' + str(number) + ' to the naughty list')
            invalid_values.append(number)
            ticket.append('NOPE')
            break

sum(invalid_values)

maybe_valid_tickets = [ticket for ticket in int_other_tickets if ticket[-1] != 'NOPE']

fields = [] # this is the entries from the valid tickets, grouped by entry
for i in range(20):
    fields.append([])
    for ticket in maybe_valid_tickets:
        fields[i].append(ticket[i])

rule_matches = []
for j in range(len(fields)): # j runs over the fields
    rule_matches.append([])
    for i in range(len(rules)): # i runs over the fields
        if all(x in rules[i][1] for x in fields[j]):
            rule_matches[j].append(i)

while max(len(x) for x in rule_matches) > 1:
    for rule_match in rule_matches:
        if len(rule_match) == 1:
            thing_to_remove = rule_match[0]
        for rule_match in rule_matches:
            rule_match.remove(thing_to_remove)

# obtain pairings by manual inspection of list
# man I am so tired

pairings = [[09,0],[12,1],[18,2],[02,3],[07,4],[19,5],[15,6],[08,7],[06,8],[01,9],[14,10],[04,11],[11,12],[05,13],[17,14],[16,15],[00,16],[03,17],[13,18],[10,19]]
my_ticket[9]*my_ticket[12]*my_ticket[18]*my_ticket[2]*my_ticket[7]*my_ticket[19]
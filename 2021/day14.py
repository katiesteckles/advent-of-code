import copy
from collections import defaultdict

with open("2021/day14_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

with open("2021/day14_test.txt", "r") as file:
    test = file.readlines()
    test = [line.strip() for line in test]

initial_chain = input[0]
instruction_dict = {}
for instruction in input[2:]:
    instruction_dict[instruction[:2]] = instruction[-1]

test_dict = {}
for instruction in test:
    test_dict[instruction[:2]] = instruction[-1]

def iterate_chain(chain, instructions):
    toinsert = []
    for i in range(len(chain)-1):
        toinsert.append(instructions[chain[i:i+2]])
    chain = ''.join([''.join(x) for x in list(zip(chain[:-1],toinsert))])+chain[-1]
    return chain

chains = [initial_chain]
for i in range(10):
    chains.append(iterate_chain(chains[-1], instruction_dict))

final_chain = list(chains[-1])

counts = []
for i in range(65,90):
    counts.append([chr(i), final_chain.count(chr(i))])

highest = max([count[1] for count in counts])
lowest = min([count[1] for count in counts if count[1] != 0])

print(highest-lowest)

# part 2

pairslist = [initial_chain[i:i+2] for i in range(len(initial_chain)-1)]
pairs_count = defaultdict(int)
for pair in pairslist:
    pairs_count[pair] += 1

def iterate_paircounts(pairs_count, instructions):
    pairs_new = defaultdict(int)
    for key in pairs_count.keys():
        pairs_new[key[0]+instructions[key]] += pairs_count[key]
        pairs_new[instructions[key]+key[1]] += pairs_count[key]
    print(pairs_new)
    return pairs_new

pairs_test = defaultdict(int)
pairs_test['CK'] = 1
pairs_test = iterate_paircounts(pairs_test,instruction_dict)

pairs_count_breakable = copy.deepcopy(pairs_count)

for i in range(40):
    pairs_count_breakable = iterate_paircounts(pairs_count_breakable,instruction_dict)

def read_out_pairs(pairs_count, original_string):
    letter_counts = defaultdict(int)
    for key in pairs_count.keys():
        letter_counts[key[0]] += pairs_count[key]
        letter_counts[key[1]] += pairs_count[key]
    letter_counts[original_string[0]] += 1
    letter_counts[original_string[-1]] += 1
    for key in letter_counts.keys():
        letter_counts[key] = letter_counts[key]//2
    return letter_counts

final_letter_counts = read_out_pairs(pairs_count_breakable,initial_chain)
highest2 = max([final_letter_counts[key] for key in final_letter_counts.keys()])
lowest2 = min([final_letter_counts[key] for key in final_letter_counts.keys() if final_letter_counts[key] != 0])

print(highest2-lowest2)
with open("day07_input.txt", "r") as file:
    rules = file.readlines()

split_rules = [rule[:-2].split(' contain ') for rule in rules]
split_split_rules = [[rule[0],rule[1].split(', ')] for rule in split_rules]

sssr = []
for rule in split_split_rules:
    sssr.append([rule[0][:-5], [[subrule[0], subrule[2:-5] if subrule[-1]=='s' else subrule[2:-4]] for subrule in rule[1]]])

bag_types_that_can_contain_shiny_gold = set()

def find_bag_type(bag_type, rules, set_to_add_to):
    for i in range(len(rules)):
        print(rules[i][0])
        for j in range(len(rules[i][1])):
            if rules[i][1][j][1] == bag_type:
                set_to_add_to.add(rules[i][0])
                print('Does contain ' + str(bag_type) + ' bags')
            else:
                print('Does not contain ' + str(bag_type) + ' bags')

find_bag_type('shiny gold', sssr, bag_types_that_can_contain_shiny_gold)

done = 0
while done == 0:
    new_bag_types = set()
    for bag in bag_types_that_can_contain_shiny_gold:
        number_of_bag_types = len(bag_types_that_can_contain_shiny_gold)
        find_bag_type(bag, sssr, new_bag_types)
    bag_types_that_can_contain_shiny_gold |= new_bag_types
    if len(bag_types_that_can_contain_shiny_gold) == number_of_bag_types:
        done = 1

# part 2

def what_bags_can_go_in_these_bags(bagcolour,number,rules):
    what_bags = []
    current_subrules = [rule[1] for rule in rules if rule[0] == bagcolour]
    # print(current_subrules)
    if current_subrules != [[['n', ' other']]]:
        for i in range(len(current_subrules[0])):
            what_bags.append([str(int(current_subrules[0][i][0])*number),current_subrules[0][i][1]])
    return what_bags

mega_bag_of_bags = what_bags_can_go_in_these_bags('shiny gold',1,sssr)
print('Initial bag list:' + str(mega_bag_of_bags))
current_list_of_bags = mega_bag_of_bags
done_this = 0
while done_this == 0:
    new_bags = []
    for i in range(len(current_list_of_bags)):
        new_bags.extend(what_bags_can_go_in_these_bags(current_list_of_bags[i][1], int(current_list_of_bags[i][0]), sssr))
    print('New bags: ' + str(new_bags))
    if new_bags == []:
        done_this = 1
    current_list_of_bags = new_bags
    mega_bag_of_bags.extend(new_bags)

total = sum(int(x[0]) for x in mega_bag_of_bags)

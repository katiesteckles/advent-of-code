import copy
input = [0, 6, 1, 7, 2, 19, 20]
list_of_numbers_said = copy.deepcopy(input)

def add_number(list_of_numbers):
    occurrences = [i+1 for i in range(len(list_of_numbers)-1) if list_of_numbers[i] == list_of_numbers[-1]]
    print(occurrences)
    if len(occurrences) == 0:
        print(str(list_of_numbers[-1]) + ' has not occurred in the list before')
        list_of_numbers.append(0)
        print(list_of_numbers)
        return(list_of_numbers)
    else:
        print(str(list_of_numbers[-1]) + ' has occurred in the list before, most recently in position ' + str(occurrences[-1]))
        list_of_numbers.append(len(list_of_numbers) - occurrences[-1])
        print(list_of_numbers)
        return(list_of_numbers)

for i in range(20):
    list_of_numbers_said = add_number(list_of_numbers_said)
print(list_of_numbers_said[2019])

# part 2

def update_dict(list_of_numbers):
    if list_of_numbers[-1] in locations_dict:
        #print('Last seen at ' + str(locations_dict[list_of_numbers[-1]]))
        list_of_numbers.append(len(list_of_numbers) - locations_dict[list_of_numbers[-1]])
        locations_dict[list_of_numbers[-2]] = len(list_of_numbers)-1
    else:
        locations_dict[list_of_numbers[-1]] = len(list_of_numbers)
        list_of_numbers.append(0)
    #print(locations_dict)
    #print(list_of_numbers)
    return(list_of_numbers)

list_of_numbers_said = copy.deepcopy(input)
locations_dict = {0: 1, 6: 2, 1: 3, 7: 4, 2: 5, 19: 6}
for i in range(30000000):
    list_of_numbers_said = update_dict(list_of_numbers_said)
print(list_of_numbers_said[29999999])
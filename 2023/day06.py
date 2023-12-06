data = [[47, 84, 74, 67], [207, 1394, 1209, 1014]]

test_data = [[7,  15,   30],[9,  40,  200]]

def generate_list_of_possibilities(time,distance):
    winners = []
    for i in range(time):
        if ((time-i)*i) > distance:
            winners.append([i, (time-i)*i])
    return winners

final_ans = 1
for i in range(len(data[0])):
    winners = generate_list_of_possibilities(data[0][i],data[1][i])
    print('In this race you could wait '+str(min([win[0] for win in winners]))+' to '+str(max([win[0] for win in winners]))+' ms and have '+str(len(winners))+' ways to win.')
    final_ans *= len(winners)

print(final_ans)

# Part B

def count_number_of_possibilities(time,distance):
    winners = 0
    for i in range(time):
        if ((time-i)*i) > distance:
            winners += 1
    return winners


data = [47847467, 207139412091014]

winners = count_number_of_possibilities(data[0], data[1])

print(winners)
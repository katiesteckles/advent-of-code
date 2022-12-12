with open("2022/day12_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

routes = [[]]
for i in range(len(input)):
    if 'S' in input[i]:
        routes[0].append([input[i].index('S'), i])  # [x,y]

def dedupe(routes_list):
    piss_off = []
    for i in range(len(routes_list)):
        for j in range(i, len(routes_list)):
            if i != j:
                if routes_list[i][-1][0] == routes_list[j][-1][0] and routes_list[i][-1][1] == routes_list[j][-1][1]:
                    if len(routes_list[i]) > len(routes_list[j]):
                        piss_off.append(routes_list[i])
                    else:
                        piss_off.append(routes_list[j])
    for dickhead in piss_off:
        if dickhead in routes_list:
            routes_list.remove(dickhead)
    return routes_list

def route_find(routes, input):
    ends = [route[-1] for route in routes]
    term_chars = set([input[end[1]][end[0]] for end in ends])
    points_visited = [str(end[0])+' '+str(end[1]) for end in ends]
    # while loop, while the end of one of the things isn't an E
    while 'E' not in term_chars and len(routes) > 0:
        new_routes = []
        for route in routes:
            current_coords = [route[-1][0],route[-1][1]]  # x,y
            current_char = input[current_coords[1]][current_coords[0]]
            if current_char == 'S':
                current_char = 'a'
            #print(current_char)
            # check all directions you're allowed to go in and add a thread going in that direction
            neighbours = []
            if 0 < current_coords[0]:  # there's space to the left
                neighbours.append([current_coords[0] - 1, current_coords[1]])
            if current_coords[0] < len(input[0])-1:  # there's space to the right
                neighbours.append([current_coords[0] + 1, current_coords[1]])
            if 0 < current_coords[1]:  # there's space above
                neighbours.append([current_coords[0], current_coords[1] - 1])
            if current_coords[1] < len(input)-1:  # there's space below
                neighbours.append([current_coords[0], current_coords[1] + 1])
            #print(neighbours)
            #print([input[neighbour[1]][neighbour[0]] for neighbour in neighbours])
            for neighbour in neighbours:
                if ord(input[neighbour[1]][neighbour[0]]) - ord(current_char) <= 1 or (current_char in 'yz' and input[neighbour[1]][neighbour[0]] == 'E'):
                    #print('You can go to '+str(neighbour))
                    if str(neighbour[0])+' '+str(neighbour[1]) not in points_visited:
                        new_routes.append(route + [neighbour])
        # if there's two threads that end in the same place, delete the longer one
        routes = dedupe(new_routes)
        ends = [route[-1] for route in routes]
        points_visited.extend([str(end[0])+' '+str(end[1]) for end in ends])
        #print(str(len(routes)) + ' current routes; endpoints '+str(ends) + '; ' + str(len(points_visited))+' points visited')
        term_chars = set([input[end[1]][end[0]] for end in ends])
    return routes

route_find(routes, input)

for route in routes:
    if input[route[-1][1]][route[-1][0]] == 'E':
        print(route)
        print(len(route)+1)

# Part B
starting_as = []
for x in range(len(input[0])-1):
    for y in range(len(input)-1):
        if input[y][x] == 'a':
            starting_as.append([x,y])

lengths = []
for a in starting_as:
    print(str(len(starting_as)-starting_as.index(a)))
    routes = route_find([[a]],input)
    for route in routes:
        if input[route[-1][1]][route[-1][0]] == 'E':
            lengths.append(len(route)+1)

print(min(lengths))
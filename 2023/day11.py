with open("2023/day11_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]
input = [x.replace('.', 'o') for x in input]

test_input = ['...#......', '.......#..', '#.........', '..........', '......#...', '.#........', '.........#', '..........', '.......#..', '#...#.....']
test_input = [x.replace('.', 'o') for x in test_input]



def as_string(seq_of_rows):
    return '\n'.join(''.join(str(i).center(1) for i in row) for row in seq_of_rows)


def galactic_expansion(galaxies):
    # find the indices of any rows with nothing in
    nothing_rows = []
    for i in range(len(galaxies)):
        if all([thing == 'o' for thing in galaxies[i]]):
            nothing_rows.append(i)
    # find the indices of any columns with nothing in and double em
    nothing_cols = []
    for j in range(len(galaxies[0])):
        if all([galaxy[j] == 'o' for galaxy in galaxies]):
            nothing_cols.append(j)
    # do expandin
    expanded_galaxy = []
    for l in range(len(galaxies)):
        if l not in nothing_rows:
            expanded_galaxy.append(galaxies[l])
        elif l in nothing_rows:
            expanded_galaxy.append(galaxies[l])
            expanded_galaxy.append(galaxies[l])
    nothing_cols.reverse()
    for col in nothing_cols:
        for k in range(len(expanded_galaxy)):
            expanded_galaxy[k] = expanded_galaxy[k][:col] + 'o' + expanded_galaxy[k][col:]
    return(expanded_galaxy)



print(as_string(test_input))
test_input = galactic_expansion(test_input)
print(as_string(test_input))

input = galactic_expansion(input)

# locate the galaxies in the expanded galaxy and make a list of coordinates
def locate_galaxies(galaxies):
    gal_goords = []
    for y in range(len(galaxies)):
        for x in range(len(galaxies[y])):
            if galaxies[y][x] == '#':
                gal_goords.append((x,y))
    return gal_goords




galaxies_test = locate_galaxies(test_input)
galaxies = locate_galaxies(input)

def find_distances(gals_list):
    distances = []
    for i in range(len(gals_list)):
        for j in range(i+1, len(gals_list)):
            distances.append(abs((gals_list[i][0]-gals_list[j][0])) + abs((gals_list[i][1]-gals_list[j][1])))
    return distances

testances = find_distances(galaxies_test)
print(sum(testances))

distances = find_distances(galaxies)
print(sum(distances))

# Part 2

# instead: count how many rows and columns are crossed and use that info


def galactic_explanation(galaxies):
    # find the indices of any rows with nothing in
    nothing_rows = []
    for i in range(len(galaxies)):
        if all([thing == 'o' for thing in galaxies[i]]):
            nothing_rows.append(i)
    # find the indices of any columns with nothing in and double em
    nothing_cols = []
    for j in range(len(galaxies[0])):
        if all([galaxy[j] == 'o' for galaxy in galaxies]):
            nothing_cols.append(j)
    return(nothing_rows, nothing_cols)


def find_distances(galaxies, nothing_rows, nothing_cols):
    # find the ones that cross a gap
    #
    distances = []
    for i in range(len(gals_list)):
        for j in range(i+1, len(gals_list)):
            distances.append(abs((gals_list[i][0]-gals_list[j][0])) + abs((gals_list[i][1]-gals_list[j][1])))
    return distances
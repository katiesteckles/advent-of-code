import copy
import re

with open("day24_input.txt", "r") as file:
    moves = file.readlines()
moves = [move[:-1] for move in moves]

test_moves = ['sesenwnenenewseeswwswswwnenewsewsw', 'neeenesenwnwwswnenewnwwsewnenwseswesw', 'seswneswswsenwwnwse', 'nwnwneseeswswnenewneswwnewseswneseene', 'swweswneswnenwsewnwneneseenw', 'eesenwseswswnenwswnwnwsewwnwsene', 'sewnenenenesenwsewnenwwwse', 'wenwwweseeeweswwwnwwe', 'wsweesenenewnwwnwsenewsenwwsesesenwne', 'neeswseenwwswnwswswnw', 'nenwswwsewswnenenewsenwsenwnesesenew', 'enewnwewneswsewnwswenweswnenwsenwsw', 'sweneswneswneneenwnewenewwneswswnese', 'swwesenesewenwneswnwwneseswwne', 'enesenwswwswneneswsenwnewswseenwsese', 'wnwnesenesenenwwnenwsewesewsesesew', 'nenewswnwewswnenesenwnesewesw', 'eneswnwswnwsenenwnwnwwseeswneewsenese', 'neswnwewnwnwseenwseesewsenwsweewe', 'wseweeenwnesenwwwswnew']

def parse_line(line):
    i = 0
    line_commands = []
    while i < len(line):
        if line[i] == 'n':
            if line[i+1] == 'e':
                line_commands.append((0.5,-1))
                i += 2
            elif line[i+1] == 'w':
                line_commands.append((-0.5,-1))
                i += 2
        elif line[i] == 's':
            if line[i+1] == 'e':
                line_commands.append((0.5,1))
                i += 2
            elif line[i+1] == 'w':
                line_commands.append((-0.5,1))
                i += 2
        elif line[i] == 'e':
            line_commands.append((1, 0))
            i += 1
        elif line[i] == 'w':
            line_commands.append((-1, 0))
            i += 1
    return line_commands

parse_line(moves[0])

def dictify_moves(moves):
    cells_dict = {}
    for line in moves:
        position = (0,0)
        line_moves = parse_line(line)
        print('Executing moves: ' + str(line_moves))
        for move in line_moves:
            position = (position[0] + move[0], position[1] + move[1])
        print('Checking cell in position ' + str(position))
        if position in cells_dict and cells_dict[position] == 'B':
            print('Cell is currently B; changing to W')
            cells_dict[position] = 'W'
        elif position not in cells_dict or cells_dict[position] == 'W':
            print('Cell is currently W; changing to B')
            cells_dict[position] = 'B'
    return cells_dict

test_dict = dictify_moves(test_moves)

sum(x =='B' for x in test_dict.values())

# part 2

def get_neighbours(x,y):
    return [(x+1, y), (x-1, y), (x+0.5, y-1), (x+0.5, y+1), (x-0.5, y-1), (x-0.5, y+1)]

# get_neighbours(0,0)

starting_dict = copy.deepcopy(cells_dict)
starting_dict = copy.deepcopy(test_dict)

def iterate_goh_grid(cells_dict):
    tiles_to_check = set(cells_dict.keys()).union(*[get_neighbours(key[0], key[1]) for key in cells_dict.keys() if cells_dict[key] == 'B'])
    dict_over = {}
    for tile in tiles_to_check:
        nbhd = get_neighbours(tile[0], tile[1])
        #print('Examining cell ' + str(tile) + '...')
        count_nbs = 0
        for cell in nbhd:
            if cell in cells_dict and cells_dict[cell] == 'B':
                count_nbs += 1
        #print('Cell has ' + str(count_nbs) + ' black neighbours')
        if tile not in cells_dict or cells_dict[tile] == 'W':
            if count_nbs == 2:
            #    print('W -> B')
                dict_over[tile] = 'B'
            #else:
            #    print('W -> W')
        elif tile in cells_dict and cells_dict[tile] == 'B':
            if count_nbs == 0 or count_nbs > 2:
            #    print('B -> W')
                dict_over[tile] = 'W'
            #else:
            #    print('B -> B')
    cells_dict.update(dict_over)
    #for key in dict_over.keys():
    #    cells_dict[key] = dict_over[key]
    print('Day ' + str(i+1) + ': ' + str(sum(x == 'B' for x in cells_dict.values())) + ' black tiles in grid (' + str(len(tiles_to_check)) + ' tiles checked)')


for i in range(100):
    iterate_goh_grid(starting_dict)
print(str(sum(x =='B' for x in starting_dict.values())) + ' black tiles in final grid')

import copy
from collections import defaultdict

with open("2021/day12_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip().split('-') for line in input]

connections = defaultdict(set)
for connect in input:
    if connect[1] != 'start': connections[connect[0]].add(connect[1])
    if connect[0] != 'start': connections[connect[1]].add(connect[0])
del connections['end']

def find_paths(dict):
    # try each of the routes out of the start node
    paths = [['start']]
    path_ends = [path[-1] for path in paths]
    while not all(x == 'end' for x in path_ends):
        newpaths = []
        for path in paths:
            newpaths.extend(extend_all_paths(dict, path))
        print(newpaths)
        print(str(len(newpaths))+' paths')
        paths = newpaths
        path_ends = [path[-1] for path in paths]
    return paths

def extend_all_paths(dict, current_path):
    if current_path[-1] == 'end':
        return [current_path]
    paths = []
    for option in dict[current_path[-1]]:
        if option.isupper() or option not in current_path:
            newpath = current_path[:]+[option]
            paths.append(newpath)
    return paths

paths = find_paths(connections)

# part 2

def extend_all_paths2(dict, current_path):
    if current_path[-1] == 'end':
        return [current_path]
    paths = []
    for option in dict[current_path[-1]]:
        if option.isupper() or option not in current_path or max(find_lower_counts(current_path,dict).values()) == 1:
            newpath = current_path[:]+[option]
            paths.append(newpath)
    return paths

def find_lower_counts(path, dict):
    counts_dict = {}
    for key in dict.keys():
        if key.islower():
            counts_dict[key] = path.count(key)
    return counts_dict

def find_paths2(dict):
    # try each of the routes out of the start node
    paths = [['start']]
    path_ends = [path[-1] for path in paths]
    while not all(x == 'end' for x in path_ends):
        newpaths = []
        for path in paths:
            newpaths.extend(extend_all_paths2(dict, path))
        print(newpaths)
        print(str(len(newpaths))+' paths')
        paths = newpaths
        path_ends = [path[-1] for path in paths]
    return paths

paths = find_paths2(connections)
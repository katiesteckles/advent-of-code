with open("2022/day07_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]
    input = [line.split(' ') for line in input[1:]]

with open("2022/test_input_07.txt","r") as file:
    test_input = file.readlines()
    test_input = [line.strip() for line in test_input]
    test_input = [line.split(' ') for line in test_input[1:]]

import re


def read_in_files(commands):
    file_locations = []
    current_path = []
    for command in commands:
        # if it's a cd command, update the path
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] != '..':
                    current_path.append(command[2])
                    print(current_path)
                elif command[2] == '..':
                    current_path = current_path[:-1]
                    print(current_path)
            if command[1] == 'ls':
                file_locations.append([tuple(current_path),0])
        # if it's a file, output a path
        if re.match('^[0-9]*$', command[0]):
            file_locations.append([tuple(current_path), int(command[0])])
            print('File! Size '+command[0])
    return file_locations


def collapse_folders(file_list):
    collapsed_list = []
    path_types = set([file[0] for file in file_list])
    for path_type in path_types:
        collapsed_list.append([path_type, sum([file[1] for file in file_list if file[0] == path_type])])
    collapsed_list.sort(key=lambda x: x[0])
    collapsed_list.sort(key=lambda x: len(x[0]))
    return collapsed_list


def measure_folders(folder_list):
    folder_sizes = []
    for folder in folder_list:
        subfolders = [subf for subf in folder_list if subf[0][:len(folder[0])] == folder[0]]
        print(folder, subfolders)
        folder_size = sum([subf[1] for subf in subfolders])
        folder_sizes.append([folder[0], folder_size])
    return folder_sizes

test_structure = read_in_files(test_input)
test_collapsed = collapse_folders(test_structure)
test_sizes = measure_folders(test_collapsed)
final_sum = sum([folder[1] for folder in measure_folders(test_collapsed) if folder[1] <= 100000])
print(final_sum)

files_list = read_in_files(input)
files_collapsed = collapse_folders(files_list)
folder_sizes = measure_folders(files_collapsed)
final_sum = sum([folder[1] for folder in measure_folders(files_collapsed) if folder[1] <= 100000])
print(final_sum)

# Part B

total_space = 70000000
whole_thing = folder_sizes[0][1]
remaining_space = total_space - whole_thing
print('Remaining space: '+str(remaining_space))
space_needed = 30000000
need_to_find = space_needed - remaining_space
print('Need to find: '+str(need_to_find))

size_of_folder_to_delete = min([folder[1] for folder in folder_sizes if folder[1] >= need_to_find])
print(size_of_folder_to_delete)
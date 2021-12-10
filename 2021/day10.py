with open("2021/day10_input.txt", "r") as file:
    input = file.readlines()
    input = [line[:-1] for line in input]

with open("2021/day10_test.txt", "r") as file:
    test_input = file.readlines()
    test_input = [line[:-1] for line in test_input]                                                                                                   < {([{{}}[<[[[<> {}]]] >[]]

    # start from left: record the type of bracket if it's open;
    # if it's closed, check if it matches the previous bracket

brack_dict = { '<': (1,0,0,0), '>': (-1,0,0,0), '{' : (0,1,0,0), '}': (0,-1,0,0), '(': (0,0,1,0), ')': (0,0,-1,0), '[': (0,0,0,1), ']':(0,0,0,-1)}

scores_dict = {')': 3,']': 57, '}': 1197, '>': 25137}

def translate_brackets(line):
    translation = []
    for bracket in line:
        translation.append(brack_dict[bracket])
    return translation

translate_brackets(input[0])


def check_bracket_sum(line):
    current_brackets = (0,0,0,0)
    for bracket in line:
        current_brackets = tuple(x + y for x, y in zip(current_brackets, brack_dict[bracket]))
    return current_brackets

issues = [check_bracket_sum(line) for line in input]

open_brackets = {'[','{','(','<'}
close_brackets = {']','}',')','>'}

def check_brackets(line):
    errmsg = 'Incomplete'
    currently_open_brackets = []
    for index, char in enumerate(line):
        if char in open_brackets:
            currently_open_brackets.append(char)
        elif char in close_brackets:
            if check_bracket_sum(char + currently_open_brackets[-1]) == (0,0,0,0):
                currently_open_brackets = currently_open_brackets[:-1]
            else:
                errmsg = char+', '+str(index)
                return errmsg
    return errmsg


errors = [check_brackets(input[i]) for i in range(len(input))]
illegals = [error.split(',') for error in errors if error != 'Incomplete']
total = sum([scores_dict[error[0]] for error in illegals])
print(total)

errors = [check_brackets(test_input[i]) for i in range(len(test_input))]
illegals = [error.split(',') for error in errors if error != 'Incomplete']
total = sum([scores_dict[error[0]] for error in illegals])
print(total)

# part 2

def missing_brackets(line):
    errmsg = 'Incomplete'
    currently_open_brackets = []
    for index, char in enumerate(line):
        if char in open_brackets:
            currently_open_brackets.append(char)
        elif char in close_brackets:
            if check_bracket_sum(char + currently_open_brackets[-1]) == (0,0,0,0):
                currently_open_brackets = currently_open_brackets[:-1]
            else:
                errmsg = char+', '+str(index)
                return errmsg
    return errmsg, currently_open_brackets

close_scores = {'(': 1,'[': 2,'{': 3,'<': 4}
errors_new = [missing_brackets(input[i]) for i in range(len(input))]
incomps = [error[1] for error in errors_new if error[0] == 'Incomplete']

def find_completion_score(incomp):
    completion_score = 0
    for bracket in incomp[::-1]:
        completion_score *=5
        completion_score += close_scores[bracket]
    return(completion_score)

completion_scores = sorted([find_completion_score(incomp) for incomp in incomps])
answer = completion_scores[len(completion_scores)//2]
print(answer)
with open("2021/day16_input.txt", "r") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

numberinhex = int(input[0],16)
numberinbinary = bin(numberinhex)[2:]

def parse_substring(string):
    # log version number
    version_number = string[:3]
    # note type
    type = string[3:6]
    if type == '100':
        literal = read_literal(string[6:])
        print('String is literal with value '+str(literal[0])+' (in decimal, '+str(int(literal[0],2))+'), total length '+str(len(literal[0])+6)+' and version number '+str(version_number)+'. The remainder is '+literal[1])
        return ['Lit', int(literal[0], 2), int(version_number, 2)], literal[1] # the length of this value plus 6 will be the length of the substring
    else:
        print('String is operator.')
        operator = read_operator(string[6:])
        print('Operator string returns the substrings ' + str(operator[0]) + '. The remainder is ' + operator[1])
        return ['Op', operator[0], sum([oporlit[-1] for oporlit in operator[0]]) + int(version_number, 2)], operator[1]

    # Returns: [[type, value(s), version], versions sum, remaining string]

def read_literal(string):
    literal_value = ''
    fivebits = 0
    while True:
        literal_value = literal_value + string[5 * fivebits + 1:(5 * fivebits) + 5]
        if string[5*fivebits] == '1':
            fivebits += 1
        elif string[5*fivebits] == '0':
            break
    return literal_value, string[5*(fivebits+1):]

def read_operator(string):
    results = []
    # if next digit is 0: read in next 15 bits and interpret as an integer; take that many digits and chop it into substrings
    if string[0] == '0':
        length_of_packet = int(string[1:16],2)
        substring_data = string[16:16+length_of_packet]
        print('Substring is '+substring_data)
        while len(substring_data) > 0:
            parsed = parse_substring(substring_data)
            results.append(parsed[0])
            substring_data = parsed[1]
        return_string = string[16+length_of_packet:]
    # if next digit is 1: read in next 11 bits and interpret as an integer; keep reading in digits until you have that many substrings
    if string[0] == '1':
        no_of_packets = int(string[1:12], 2)
        string = string[12:]
        print('Searching for '+str(no_of_packets)+' substrings in '+string)
        for i in range(no_of_packets):
            parsed = parse_substring(string)
            results.append(parsed[0])
            string = parsed[1]
        return_string = string
    return results, return_string

# read_literal('101111111000101000')
# parse_substring('110100101111111000101000')
# parse_substring('110100101111111000101000')
# parse_substring('11101110000000001101010000001100100000100011000001100000')
# parse_substring('00111000000000000110111101000101001010010001001000000000')

parse_substring(numberinbinary)

# Part 2

def prod(list):
    product = 1
    for item in list:
        product  *= int(item)
    return product

def full_parse_substring(string):
    # log version number
    version_number = string[:3]
    # note type
    type = string[3:6]
    if type == '100':
        literal = read_literal(string[6:])
        print('String is literal with value '+str(literal[0])+' (in decimal, '+str(int(literal[0],2))+'), total length '+str(len(literal[0])+6)+' and version number '+str(version_number)+'. The remainder is '+literal[1])
        return ['Lit', int(literal[0], 2)], literal[1] # [lit, literal value], string remainder
    elif type == '000':
        print('String is sum operator.')
        operator = read_operator(string[6:])
        print('Operator string returns the substrings ' + str(operator[0]) + '. The remainder is ' + operator[1])
        return ['Op', operator[0], sum([oporlit[-1] for oporlit in operator[0]])], operator[1] # [op, values from contained substrings, sum of that], string remainder
    elif type == '001':
        print('String is product operator.')
        operator = read_operator(string[6:])
        print('Operator string returns the substrings ' + str(operator[0]) + '. The remainder is ' + operator[1])
        return ['Op', operator[0], prod([oporlit[-1] for oporlit in operator[0]])], operator[1]
    elif type == '010':
        print('String is minimum operator.')
        operator = read_operator(string[6:])
        print('Operator string returns the substrings ' + str(operator[0]) + '. The remainder is ' + operator[1])
        return ['Op', operator[0], min([oporlit[-1] for oporlit in operator[0]])], operator[1]
    elif type == '011':
        print('String is maximum operator.')
        operator = read_operator(string[6:])
        print('Operator string returns the substrings ' + str(operator[0]) + '. The remainder is ' + operator[1])
        return ['Op', operator[0], max([oporlit[-1] for oporlit in operator[0]])], operator[1]
    elif type == '101':
        print('String is \'greater than\' operator.')
        operator = read_operator(string[6:])
        print('Operator string returns the substrings ' + str(operator[0]) + '. The remainder is ' + operator[1])
        if operator[0][0][-1] > operator[0][1][-1]:
            return ['Op', operator[0], 1], operator[1]
        else:
            return ['Op', operator[0], 0], operator[1]
    elif type == '110':
        print('String is \'less than\' operator.')
        operator = read_operator(string[6:])
        print('Operator string returns the substrings ' + str(operator[0]) + '. The remainder is ' + operator[1])
        if operator[0][0][-1] < operator[0][1][-1]:
            return ['Op', operator[0], 1], operator[1]
        else:
            return ['Op', operator[0], 0], operator[1]
    elif type == '111':
        print('String is \'equal to\' operator.')
        operator = read_operator(string[6:])
        print('Operator string returns the substrings ' + str(operator[0]) + '. The remainder is ' + operator[1])
        if operator[0][0][-1] == operator[0][1][-1]:
            return ['Op', operator[0], 1], operator[1]
        else:
            return ['Op', operator[0], 0], operator[1]

    # Returns: [[type, value(s), version], versions sum, remaining string]

def read_operator(string):
    results = []
    # if next digit is 0: read in next 15 bits and interpret as an integer; take that many digits and chop it into substrings
    if string[0] == '0':
        length_of_packet = int(string[1:16],2)
        substring_data = string[16:16+length_of_packet]
        print('Substring is '+substring_data)
        while len(substring_data) > 0:
            parsed = full_parse_substring(substring_data)
            results.append(parsed[0])
            substring_data = parsed[1]
        return_string = string[16+length_of_packet:]
    # if next digit is 1: read in next 11 bits and interpret as an integer; keep reading in digits until you have that many substrings
    if string[0] == '1':
        no_of_packets = int(string[1:12], 2)
        string = string[12:]
        print('Searching for '+str(no_of_packets)+' substrings in '+string)
        for i in range(no_of_packets):
            parsed = full_parse_substring(string)
            results.append(parsed[0])
            string = parsed[1]
        return_string = string
    return results, return_string

full_parse_substring(numberinbinary)
with open("2024/day09.txt", "r") as file:
    input = file.readlines()
    input = [list(line.strip()) for line in input][0]

test_input = list('2333133121414131402')

def crunch_input(input, type):
    input = [int(x) for x in input]
    number_segs = input[type::2]
    crunched_input = []
    for i in range(len(number_segs)):
        for j in range(number_segs[i]):
            crunched_input.append(i)
    return crunched_input

# crunched = crunch_input(test_input, 0)

def alt_readin(input):
    #print(input)
    crunched = crunch_input(input, 0)
    readout = []
    front = True
    i = 0
    while len(crunched) > 0:
        #print(i, crunched, front)
        if front == True:
            if int(input[i]) > len(crunched):
                readout = crunched[::-1] + readout
                crunched = []
            else:
                for j in range(int(input[i])):
                    readout.append(crunched[0])
                    crunched = crunched[1:]
            #print(readout)
            front = False
        elif front == False:
            if int(input[i]) > len(crunched):
                readout.extend(crunched)
                crunched = []
            else:
                for j in range(int(input[i])):
                    readout.append(crunched[-1])
                    crunched = crunched[:-1]
            #print(readout)
            front = True
        # print(i)
        i += 1
    return readout

readout = alt_readin(input)

def checksum(readout):
    total = 0
    for i in range(len(readout)):
        total += int(readout[i]) * i
    return total

print(checksum(readout))

# Part Beta

# instead read in the crunched list as [[0, 6], [1, 2]... etc then compare the lengths of chunks at the end to the list of gaps until you find one that fits, then remove that gap length from the list and put in a blank gap as needed
input = [11404017, 13768789]

mod_value = 20201227

def encrypt_steps(subject, loop_times):
    value = 1
    for i in range(loop_times):
        value = (value * subject) % mod_value
    return value


def encrypt_finder(subject, key_to_find):
    i = 1
    found_it = 0
    value = 1
    while found_it == 0:
        value = (value * subject) % mod_value
        if value == key_to_find:
            print('I found it! The loop size is ' + str(i) + ' and gives ' + str(value))
            found_it = 1
        else:
            i += 1
    return i


loop_size_1 = encrypt_finder(7,input[0])
loop_size_2 = encrypt_finder(7,input[1])

encrypt_steps(input[0],loop_size_2)
encrypt_steps(input[1],loop_size_1)

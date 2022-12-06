with open("2022/day06_input.txt","r") as file:
    input = file.readlines()
    input = [line.strip() for line in input][0]


def window_check(window,n):
    set_chars = set([letter for letter in window])
    return len(set_chars) == n


def find_window(input_string,n):
    for i in range(n,len(input_string) + 1):
        if window_check(input_string[i - n:i],n):
            return i


test_1 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

find_window(test_1,4)
find_window(input,4)
find_window(input,14)

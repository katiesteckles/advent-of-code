import copy
import re
with open("day18_input.txt", "r") as file:
    lines = file.readlines()

def resolve_lr(input_string): # the input string should not contain brackets
    total = 0
    # work from left to right and resolve it: if it's a number, put it in a thingand, and then add/multiply the thingtrix
    return total

# something with brackets
brackets = count(brackets)

while brackets > 0:
    # find a pair of brackets with no brackets inside (using a regex)
    # replace the brackets and their contents with the resolve_lr of the contents of the bracket
    # recount the brackets
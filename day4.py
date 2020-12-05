with open("day4_input.txt", "r") as file:
    data = file.readlines()

data = [x[:-1] for x in data]  # raw lines
entries = ['']*1000
row = 0
for i in range(len(data)):  # puts the lines into separate entries
    if data[i] != '':
        if entries[row] == '':
            entries[row] = data[i]
        else:
            entries[row] = entries[row] + ' ' + data[i]
    else:
        row += 1

entry_split = [entry.split(' ') for entry in entries] # splits each entry which is a long string into a list of lists
splitentries = []
for splitentry in entry_split:
    splitentries.append([x.split(':') for x in splitentry])  #splits those entries on the colon to make a list of lists of pairs

allheaders = []
for splitentry in entry_split:
    headers = []
    headers.append([x.split(':')[0] for x in splitentry])
    allheaders.append(headers)

has_all_fields = []
for i in range(len(allheaders)):
    if 'byr' in allheaders[i][0] and 'iyr' in allheaders[i][0] and 'eyr' in allheaders[i][0] and 'hgt' in allheaders[i][0] and 'hcl' in allheaders[i][0] and 'ecl' in allheaders[i][0] and 'pid' in allheaders[i][0]:
        has_all_fields.append(splitentries[i])

import re

regexestocheck = dict(byr=re.compile("^[\d]{4}$"),
                      iyr=re.compile("^[\d]{4}$"),
                      eyr=re.compile("^[\d]{4}$"),
                      hgt=re.compile("^[\d]+(cm|in)$"),
                      hcl=re.compile("^#[\da-f]{6}$"),
                      ecl=re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$"),
                      pid=re.compile("^\d{9}$"),
                      cid=re.compile(".*"))

matches_regex = []
def regexes_check(input, regexestocheck):
    for i in range(len(input)):
        isvalid = True
        for j in range(len(input[i])):
            regex = regexestocheck[input[i][j][0]]
            isvalid = isvalid and regex.match(input[i][j][1])
        if isvalid:
            matches_regex.append(input[i])

regexes_check(has_all_fields,regexestocheck)

def check_byr(year):
    return int(year) >= 1920 and int(year) <= 2002

def check_iyr(year):
    return int(year) >= 2010 and int(year) <= 2020

def check_eyr(year):
    return int(year) >= 2020 and int(year) <= 2030

def check_hgt(height):
    if height[-2:] == 'cm':
        return int(height[:-2]) >= 150 and int(height[:-2]) <= 193
    if height[-2:] == 'in':
        return int(height[:-2]) >= 59 and int(height[:-2]) <= 76

# byr (Birth Year) - four digits; at least 1920 and at most 2002.  ^[\d]{4}}$
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.  ^[\d]{4}}$
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030. ^[\d]{4}}$
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193. ^[\d]+(cm|in)$
#   If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.  ^#[\da-f]{6}$
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth. ^(amb|blu|brn|gry|grn|hzl|oth)$
# pid (Passport ID) - a nine-digit number, including leading zeroes. ^\d{9}$
# cid (Country ID) - ignored, missing or not.

its_totally_fine = []
def checky_mc_checkface(input):
    for i in range(len(input)):
        dicttotest = dict(input[i])
        isvalid = check_byr(dicttotest['byr']) and check_iyr(dicttotest['iyr']) and check_eyr(dicttotest['eyr']) and check_hgt(dicttotest['hgt'])
        if isvalid:
            its_totally_fine.append(input[i])






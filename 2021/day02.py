with open("2021/day02_input.txt", "r") as file:
    commands = file.readlines()

commands = [x[:-1].split(" ") for x in commands]

total_vert_distance = sum([int(x[1]) for x in commands if x[0] == "down"]) - sum([int(x[1]) for x in commands if x[0] == "up"])
total_horz_distance = sum([int(x[1]) for x in commands if x[0] == "forward"])

answer = total_vert_distance *  total_horz_distance

# part 2

test_data = [['forward','5'],['down','5'],['forward','8'],['up','3'],['down','8'],['forward','2']]

horz_dep_aim=[0,0,0]
def move(hda, commd):
    if commd[0] == "down":
        hda[2]+= int(commd[1])
    elif commd[0] == "up":
        hda[2]-= int(commd[1])
    elif commd[0] == "forward":
        hda[0] += int(commd[1])
        hda[1] += (int(commd[1]) * hda[2])
    return(hda)

for commd in commands:
    move(horz_dep_aim,commd)

print(horz_dep_aim[0] * horz_dep_aim[1])



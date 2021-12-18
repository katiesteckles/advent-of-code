import copy
target_area = [[277, 318], [-92, -53]]

def iterate_time(pos, vel):
    for i in range(2):
        pos[i] += vel[i]
    if vel[0] > 0:
        vel[0] -= 1
    elif vel[0] < 0:
        vel[0] += 1
    vel[1] -= 1
    return(pos, vel)

def run_vel_value(vel, target):
    initial_vel = copy.deepcopy(vel)
    pos = [0,0]
    steps = 0
    maxy = pos[1]
    #print('Launching with velocity '+str(vel))
    while pos[0] <= target[0][1] and pos[1] >= target[1][0]:
        iterate_time(pos,vel)
        #print(pos)
        steps += 1
        maxy = max(maxy, pos[1])
        if target[0][0] <= pos[0] <= target[0][1] and target[1][0] <= pos[1] <= target[1][1]:
            print('Initial velocity (' + str(initial_vel[0]) + ', '+str(initial_vel[1]) + '), after '+str(steps)+': position ('+str(pos[0])+', '+str(pos[1])+'). Max height: '+str(maxy)+'.')
            return True, maxy, initial_vel
    return False, maxy, initial_vel

max_heights = []
winning_velocities = []
for xvel in range(0,319):
    for yvel in range(0,100):
        result = run_vel_value([xvel, yvel], target_area)
        if result[0] == True:
            max_heights.append(result[1])
            winning_velocities.append(result[2])

print(max(max_heights))
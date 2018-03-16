# From calculation, it is expected that the local minimum occurs at x=9/4

cur_x = 6 # The algorithm starts at x=6
gamma = 0.01 # step size multiplier
precision = 0.00001
previous_step_size = 1/precision; # some large value

df = lambda x: 4 * x**3 - 9 * x**2

while previous_step_size > precision:
    #print(previous_step_size)
    prev_x = cur_x
    #print(prev_x)
    cur_x += -gamma * df(prev_x)
    print(cur_x)
    previous_step_size = abs(cur_x - prev_x)

print("The local minimum occurs at %f" % cur_x)

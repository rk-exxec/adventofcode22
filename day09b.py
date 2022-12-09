import numpy as np

with open("day09_input.txt") as f:
    lines = f.readlines()

knots = np.zeros((10,2), dtype=np.int32)

all_tail_pos = set([(0,0)])

for lin in lines:
    tr_dir, tr_len = lin.strip().split(" ")

    for i in range(int(tr_len)):
        if tr_dir == "U":
            knots[0] += np.array([0,1])
        elif tr_dir == "D":
            knots[0] += np.array([0,-1])
        elif tr_dir == "R":
            knots[0] += np.array([1,0])
        elif tr_dir == "L":
            knots[0] += np.array([-1,0])

        for i in range(1, len(knots)):
            delta = knots[i-1] - knots[i]
            if np.any(abs(delta) > 1):

                idx = abs(delta).argmax()
                mov_delta = delta
                mov_delta[idx] = np.sign(mov_delta[idx]) * 1
                knots[i] += mov_delta
                # if i == len(knots)-1: 
        all_tail_pos.add(tuple(knots[-1]))

zero_x = min(knots.T[0].min(),0)
zero_y = min(knots.T[1].min(),0)
view_width = max(knots.T[0].max() + 1 - zero_x,5)
view_height = max(knots.T[1].max() + 1 - zero_y,5)
vis = np.zeros((view_width,view_height), dtype=np.int8)
true_pos = knots - np.array([zero_x,zero_y])
vis[true_pos.T[0], true_pos.T[1]] = 1

print(vis)

print(len(all_tail_pos))
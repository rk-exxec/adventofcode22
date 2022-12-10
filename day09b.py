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
                mov_delta = np.sign(delta)
                knots[i] += mov_delta
        all_tail_pos.add(tuple(knots[-1]))


print(len(all_tail_pos))
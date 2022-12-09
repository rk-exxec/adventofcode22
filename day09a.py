import numpy as np

with open("day09_input.txt") as f:
    lines = f.readlines()

head_pos = np.array([0,0])

tail_pos = np.array([0,0])

all_tail_pos = set([(0,0)])

for lin in lines:
    tr_dir, tr_len = lin.split(" ")

    for i in range(int(tr_len)):
        if tr_dir == "U":
            head_pos += np.array([0,1])
        elif tr_dir == "D":
            head_pos += np.array([0,-1])
        elif tr_dir == "R":
            head_pos += np.array([1,0])
        elif tr_dir == "L":
            head_pos += np.array([-1,0])

        delta = head_pos - tail_pos
        if np.any(abs(delta) > 1):

            idx = abs(delta).argmax()
            mov_delta = delta
            mov_delta[idx] = np.sign(mov_delta[idx]) * 1
            tail_pos += mov_delta
            all_tail_pos.add(tuple(tail_pos))

print(len(all_tail_pos))
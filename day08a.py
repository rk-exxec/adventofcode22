import numpy as np


def load():
    with open("day08_input.txt") as f:
        lines = f.readlines()

    width = len(lines[0].strip())

    height = len(lines)

    arr = np.zeros((width, height), dtype=np.int8)

    for i,line in enumerate(lines):
        line = line.strip()
        for j,num in enumerate(line):
            arr[i,j] = int(num)
    return arr, width, height

trees, w, h = load()

num_trees_vis = 0

for i,j in np.ndindex(trees.shape):
    # edge trees
    if i == 0 or j == 0 or i == w-1 or j == h-1:
        num_trees_vis += 1
    else:
        tr_height = trees[i,j]
        if tr_height > trees[i,:j].max() or tr_height > trees[i,j+1:].max() or \
            tr_height > trees[:i, j].max() or tr_height > trees[i+1:, j].max():
            num_trees_vis += 1

print(num_trees_vis)
        


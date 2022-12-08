import numpy as np

from day08a import load


trees, w, h = load()

max_score = 0

for i,j in np.ndindex(trees.shape):
    # edge trees
    if i == 0 or j == 0 or i == w-1 or j == h-1:
        continue
    else:
        tr_height = trees[i,j]
        # up
        idx = np.argwhere(trees[:i,j] >= tr_height)
        if not idx.size: up = i
        else: up = i - idx.max()
        # down
        idx = np.argwhere(trees[i+1:,j] >= tr_height)
        if not idx.size: down = h - (i + 1)
        else: down = idx.min() + 1
        # left
        idx = np.argwhere(trees[i,:j] >= tr_height)
        if not idx.size: left = j
        else: left = j - idx.max()
        # right
        idx = np.argwhere(trees[i,j+1:] >= tr_height)
        if not idx.size: right = w - (j + 1)
        else: right = idx.min() + 1

        score = up*down*left*right
        if score > max_score: max_score = score

print(max_score)

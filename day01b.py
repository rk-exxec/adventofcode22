import numpy as np

with open("day01_input.txt") as inp:
    lines = inp.readlines()

elfs = []
elfs.append(0)
idx = 0

for ln in lines:
    ln = ln.strip()
    if ln == "": 
        idx+=1
        elfs.append(0)
    else:
        elfs[idx] += int(ln)

sort = sorted(elfs,reverse=True)
print(str(sum(sort[:3])))
import numpy as np

with open("day1_input.txt") as inp:
    lines = inp.readlines()

cur_max_cal = 0
cur_cal = 0
for ln in lines:
    ln = ln.strip()
    if ln == "": 
        if cur_max_cal < cur_cal: cur_max_cal = cur_cal
        cur_cal = 0
    else:
        cur_cal += int(ln)

print(cur_max_cal)
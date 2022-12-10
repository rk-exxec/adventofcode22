import numpy as np

with open("day10_input.txt") as f:
    lines = f.readlines()

cycle = 0
num_ops = 0
add_val = 0
progr_pointer = 0
X = 1
total = 0

crt = np.zeros((6,40), dtype=bool)

while(True):
    if num_ops:
        num_ops -= 1
        sprite_visible = abs((cycle % 40) - X) <= 1
        crt[cycle // 40, cycle % 40] = sprite_visible
        cycle +=1

    if num_ops == 0:
        X += add_val
        try:
            line = lines[progr_pointer].strip()
            progr_pointer += 1
        except Exception as ex:
            print(ex)
            break
        if line == "noop":
            num_ops = 1
            add_val = 0
        else:
            num_ops = 2
            add_val = int(line.split(" ")[-1])

for i in range(6):
    for j in range(40):
        print("#" if crt[i,j] else '.', end="")
    print("")




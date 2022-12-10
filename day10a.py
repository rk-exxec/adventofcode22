with open("day10_input.txt") as f:
    lines = f.readlines()

cycle = 0
num_ops = 0
add_val = 0
progr_pointer = 0
X = 1
total = 0

while(True):
    if num_ops:
        num_ops -= 1
        cycle +=1
        if ((cycle - 20) % 40) == 0:
            total += (cycle * X)
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

        
print(total)



from collections import deque

with open("day05_input.txt") as file:
    lines = file.readlines()

crates = lines[:8]

moves = lines[10:]

stacks = [deque() for _ in range(9)]
# populate initial stacks
for i, line in enumerate(reversed(crates)):
    line = line.strip()
    cur_stack = 0
    for i in range(1, len(line)+1, 4):
        if line[i] != " ":
            stacks[cur_stack].append(line[i])
            
        cur_stack += 1

#movement
for mov in moves:
    pars = mov.strip().split(" ")
    num_moves = int(pars[1])
    from_stack = int(pars[3])-1 # subtract bc instructions give 1 based index
    to_stack = int(pars[5])-1
    for i in range(num_moves):
        stacks[to_stack].append(stacks[from_stack].pop())

result = ''.join([x.pop() for x in stacks])

print(result)
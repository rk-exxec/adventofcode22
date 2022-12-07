from day07 import *

with open("day07_input.txt") as file:
    lines = file.readlines()

root = read_filetree(lines)

store: dict[str, int] = dict()

total_size = root.get_size(store)

free_space = (70000000 - total_size)

missing_size = 30000000 - free_space

cur_sel_del_size = 70000000
for k,v in store.items():
    if v >= missing_size and v < cur_sel_del_size:
        cur_sel_del_size = v

print(cur_sel_del_size)
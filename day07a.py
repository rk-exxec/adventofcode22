from day07 import *

with open("day07_input.txt") as file:
    lines = file.readlines()

root = read_filetree(lines)

store: dict[str, int] = dict()

root.get_size(store)

total_possible_del_size = 0
for k,v in store.items():
    if v < 100000:
        total_possible_del_size += v

print(total_possible_del_size)


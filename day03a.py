def get_item_value(item):
    asc = ord(item)
    if asc <= 91:
        return asc - 65 + 27
    elif asc <= 122:
        return asc - 97 + 1

with open("day03_input.txt") as inp:
    lines = inp.readlines()


sum = 0

for line in lines:
    line = line.strip()
    first_comp = set(line[:len(line)//2])
    second_comp = set(line[len(line)//2:])

    intersection = first_comp.intersection(second_comp)
    duplitcate = list(intersection)[0]
    sum += get_item_value(duplitcate)

print(sum)

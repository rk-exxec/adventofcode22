def get_item_value(item):
    asc = ord(item)
    if asc <= 91:
        return asc - 65 + 27
    elif asc <= 122:
        return asc - 97 + 1

with open("day03_input.txt") as inp:
    lines = inp.readlines()


sum = 0

for i in range(0,len(lines),3):
    first = set(lines[i].strip())
    second = set(lines[i+1].strip())
    third = set(lines[i+2].strip())

    intersection = first & second & third
    duplicate = list(intersection)[0]
    sum += get_item_value(duplicate)

print(sum)

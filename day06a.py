
with open("day06_input.txt") as file:
    lines = file.readlines()

line = lines[0].strip()

for i in range(4, len(line)):
    substr = line[i-4:i]
    if(len(set(substr)) == len(substr)): 
        print(i)
        break
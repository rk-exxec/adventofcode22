with open("day04_input.txt") as file:
    lines = file.readlines()

total_overlaps = 0
for line in lines:
    p1,p2 = line.strip().split(",")
    p1_low,p1_hi = p1.split("-")
    p2_low,p2_hi = p2.split("-")

    range1 = set(range(int(p1_low),int(p1_hi)+1))
    range2 = set(range(int(p2_low),int(p2_hi)+1))

    if range1.issubset(range2) or range2.issubset(range1): 
        total_overlaps +=1
        print(range1, range2)
    

print(total_overlaps)
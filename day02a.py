with open("day02_input.txt") as file:
    lines = file.readlines()

results = {"A": {"X": 3, "Y": 6, "Z": 0},
          "B": {"X": 0, "Y": 3, "Z": 6},
          "C": {"X": 6, "Y": 0, "Z": 3}}

my_points = {"X": 1, "Y": 2, "Z": 3}

score = 0

for ln in lines:
    ln = ln.strip()
    they, me = ln.split(" ")
    score += results[they][me] + my_points[me]

print(score)
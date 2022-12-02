with open("day02_input.txt") as file:
    lines = file.readlines()

need_top_play = {   
                "A": {"X": "C", "Y": "A", "Z": "B"},
                "B": {"X": "A", "Y": "B", "Z": "C"},
                "C": {"X": "B", "Y": "C", "Z": "A"}
                }

strategy = {"X": 0, "Y": 3, "Z": 6}

my_points = {"A": 1, "B": 2, "C": 3}

score = 0

for ln in lines:
    ln = ln.strip()
    they, me = ln.split(" ")
    score += strategy[me] + my_points[need_top_play[they][me]]


print(score)
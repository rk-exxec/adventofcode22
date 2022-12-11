with open("day11_input.txt") as f:
    lines = f.readlines()

class Monkey:
    def __init__(self, number):
        self.items = list()
        self.operation = None
        self.targets: list[Monkey] = list()
        self.test_divider = 0

    def catch_item(self, item):
        self.items.append(item)

    def throw_items(self):
        for item in self.items:
            new = self.do_operation(item)
            target = self.select_target(new)
            target.catch_item(new)
        
        self.items.clear()
    
    def do_operation(self, item):
        old = item
        new = 0
        eval(self.operation)
        return new // 3

    def select_target(self, item):
        if (item % self.test_divider) == 0:
            return self.targets[0]
        else:
            return self.targets[1]


# build structs
monkeys = list()
for line in lines:
    line = line.strip()
    if line.startswith("Monkey"):
        monkeys.append(Monkey())
    else:
        


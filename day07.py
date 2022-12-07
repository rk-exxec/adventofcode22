class Node:
    def __init__(self, name, parent) -> None:
        self.name: str = name
        self.parent: Node = parent

    def is_file(self): 
        raise NotImplementedError()

    def get_size(self, store=None) -> int:
        raise NotImplementedError()

    def __str__(self):
        return self.name

    def print(self, indent):
        return NotImplementedError()

    def path(self) -> str:
        if self.parent:
            return self.parent.path() + self.name + "/"
        else:
            return self.name


class Dir(Node):
    def __init__(self, name, data: list[Node] = None, parent = None) -> None:
        super().__init__(name, parent)
        self.content = data if data else list()

    def __str__(self):
        return f"{self.name} (dir)"

    def __repr__(self):
        return f"(dir {self.name})  {self.parent=}"

    def is_file(self):
        return False

    def get_size(self, store:dict[str,int]=None):
        size = 0
        for node in self.content:
            size += node.get_size(store)
        if not store is  None:
            store[self.path()] = size
        return size

    def add_child(self, node: Node):
        if not node in self.content:
            self.content.append(node)
            node.parent = self

    def get_child(self, name):
        for child in self.content:
            if child.name == name:
                return child
        else:
            return None

    def print(self, indent):
        return "  "*indent + "- " + str(self) + "\n" + "".join([x.print(indent+1) for x in self.content])


class File(Node):
    def __init__(self, name, size: int, parent) -> None:
        super().__init__(name, parent)
        self.size = size
    
    def __str__(self):
        return f"{self.name} (file, size={self.size})"
    
    def __repr__(self):
        return f"(file {self.name})  {self.size=}"

    def is_file(self):
        return True

    def get_size(self, store=None) -> int:
        return self.size

    def print(self, indent):
        return "  "*indent + "- " + str(self) + "\n"

    
def read_filetree(commands):
    root = Dir("/")
    cur_dir = root

    for lin in commands:
        lin = lin.strip()
        # is command
        if lin.startswith("$"):
            if " cd " in lin:
                newdir = lin.split(" ")[-1]
                if newdir == "/": continue
                elif newdir == "..": cur_dir = cur_dir.parent
                else: cur_dir = cur_dir.get_child(newdir)
            elif "ls" in lin:
                continue
        else:
            if lin.startswith("dir"):
                new_dir = lin.split(" ")[-1]
                cur_dir.add_child(Dir(new_dir, parent=cur_dir))
            else:
                file_size, file_name = lin.split(" ")
                cur_dir.add_child(File(file_name, int(file_size), cur_dir))
    return root

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChildren(self, name):
        self.children.append(Node(name))

    def depthFirst(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirst(array)
        return array

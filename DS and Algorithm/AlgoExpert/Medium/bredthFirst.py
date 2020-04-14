class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def breadthFirst(self, array):
        queue = [self]
        while len(queue):
            current = queue.pop(0)
            array.append(current)
            for child in self.children:
                queue.append(child)
        return array

# def findclosestvalueinBST(tree, target):
#     return findclosestvalueinBSThelper(tree, target, float("inf"))

# def findclosestvalueinBSThelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value

#     if target < tree.value:
#         return findclosestvalueinBSThelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findclosestvalueinBSThelper(tree.right, target, closest)
#     else:
#         return closest


def findclosestvalueinBST(tree, target):
    return findclosestvalueinBSThelper(tree, target, float("inf"))


def findclosestvalueinBSThelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.tree
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

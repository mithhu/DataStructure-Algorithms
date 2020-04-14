# time - o(n) space- o(n)

# def invertBinaryTree(tree):
#     queue = [tree]
#     while len(queue):
#         current = queue.pop(0)
#         swapLeftAndRight(tree)
#         queue.append(current.left)
#         queue.append(current.right)


# def swapLeftAndRight(tree):
#     tree.left, tree.right = tree.right, tree.left

# time - o(n) space- o(log(n))
def inverseBinaaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    inverseBinaaryTree(tree.left)
    inverseBinaaryTree(tree.right)


def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left
